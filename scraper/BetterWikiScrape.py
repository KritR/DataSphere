import requests
import bz2
import subprocess

# Library for parsing HTML/XML
from bs4 import BeautifulSoup

import sys
from keras.utils import get_file
import os
import mwparserfromhell
import re

#keras_home = '/home/sambruns2000/.keras/datasets/'
data_dir = '/home/sambruns2000/wikidata/'
base_url = 'https://dumps.wikimedia.org/enwiki/'
index = requests.get(base_url).text
soup_index = BeautifulSoup(index, 'html.parser')

# Find the links that are dates of dumps
dumps = [a['href'] for a in soup_index.find_all('a') if
        a.has_attr('href')]

dump_url = base_url + '20200101/'

# Retrieve the html
dump_html = requests.get(dump_url).text

# Convert to a soup
soup_dump = BeautifulSoup(dump_html, 'html.parser')

# Find li elements with the class file
soup_dump.find_all('li', {'class': 'file'}, limit = 10)

files = []

# Search through all files
for file in soup_dump.find_all('li', {'class': 'file'}):
    text = file.text
    # Select the relevant files
    if 'pages-articles' in text and '-mul' not in text:
        files.append((text.split()[0], text.split()[1:]))

print(files[:5])


files_to_download = [file[0] for file in files if '.xml-p' in file[0]]
print()
print(files_to_download[0:20])

data_paths = []
file_info = []


# Iterate through each file
for file in files_to_download:
    path = data_dir + file
    
    # Check to see if the path exists (if the file is already downloaded)
    if not os.path.exists(data_dir + file):
        print('Downloading')
        # If not, download the file
        data_paths.append(get_file(file, dump_url))
        # Find the file size in MB
        file_size = os.stat(path).st_size / 1e6
        
        # Find the number of articles
        file_articles = int(file.split('p')[-1].split('.')[-2]) - int(file.split('p')[-2])
        file_info.append((file, file_size, file_articles))
        
    # If the file is already downloaded find some information
    else:
        data_paths.append(path)
        # Find the file size in MB
        file_size = os.stat(path).st_size / 1e6
        
        # Find the number of articles
        file_number = int(file.split('p')[-1].split('.')[-2]) - int(file.split('p')[-2])
        file_info.append((file.split('-')[-1], file_size, file_number))

data_path = data_paths[-1]

def process_article(title, text, timestamp, template = 'Infobox event'):
    """Process a wikipedia article looking for template"""
    
    # Create a parsing object
    wikicode = mwparserfromhell.parse(text)
    
    # Search through templates for the template
    matches = wikicode.filter_templates(matches = template)
    
    # Filter out errant matches
    matches = [x for x in matches if x.name.strip_code().strip().lower() == template.lower()]
    
    if len(matches) >= 1:
        # template_name = matches[0].name.strip_code().strip()

        # Extract information from infobox
        properties = {param.name.strip_code().strip(): param.value.strip_code().strip() 
                      for param in matches[0].params
                      if param.value.strip_code().strip()}

        # Find approximate length of article
        text_length = len(wikicode.strip_code().strip())

        return (title, properties, timestamp, text_length)

import xml.sax

class WikiXmlHandler(xml.sax.handler.ContentHandler):
    """Parse through XML data using SAX"""
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._events = []
        self._article_count = 0
        self._non_matches = []

    def characters(self, content):
        """Characters between opening and closing tags"""
        if self._current_tag:
            self._buffer.append(content)

    def startElement(self, name, attrs):
        """Opening tag of element"""
        if name in ('title', 'text', 'timestamp'):
            self._current_tag = name
            self._buffer = []

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)

        if name == 'page':
            self._article_count += 1
            # Search through the page to see if the page is a event
            event = process_article(**self._values, template = 'Infobox event')
            # Append to the list of event
            if event:
                self._events.append(event)

"""
handler = WikiXmlHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)

for i, line in enumerate(subprocess.Popen(['bzcat'],
    stdin = open(data_path),
    stdout = subprocess.PIPE).stdout):
    parser.feed(line)

    if len(handler._events) > 2:
        break

print(f'Searched through {handler._article_count} articles to find 3 events.')
print(handler._events[0]) 
"""

import gc
import json

def find_events(data_path, limit = None, save = True):
    """Find all the event articles from a compressed wikipedia XML dump.
       `limit` is an optional argument to only return a set number of books.
        If save, events are saved to partition directory based on file name"""

    # Object for handling xml
    handler = WikiXmlHandler()

    # Parsing object
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)

    limit = 3000

    # Iterate through compressed file
    for i, line in enumerate(subprocess.Popen(['bzcat'],
                             stdin = open(data_path),
                             stdout = subprocess.PIPE).stdout):
        try:
            parser.feed(line)
        except StopIteration:
            break

        # Optional limit
        if limit is not None and len(handler._events) >= limit:
            return handler._events

    if save:
        partition_dir = '/data/wiki/partitions/'
        # Create file name based on partition name
        p_str = data_path.split('-')[-1].split('.')[-2]
        out_dir = partition_dir + f'{p_str}.ndjson'

        # Open the file
        with open(out_dir, 'w') as fout:
            # Write as json
            for book in handler._events:
                fout.write(json.dumps(event) + '\n')

        print(f'{len(os.listdir(partition_dir))} files processed.', end = '\r')

    # Memory management
    del handler
    del parser
    gc.collect()
    return None

partitions = [data_dir + file for file in os.listdir(data_dir) if 'xml-p' in file]

from multiprocessing import Pool
import tqdm
from timeit import default_timer as timer

# List of lists to single list
from itertools import chain

# Sending keyword arguments in map
from functools import partial

# Create a pool of workers to execute processes
pool = Pool(processes = 16)

start = timer()

# Map (service, tasks), applies function to each partition
for x in tqdm.tqdm(pool.imap_unordered(find_events, partitions), total = len(partitions)):
    results.append(x)

pool.close()
pool.join()

end = timer()
print(f'{end - start} seconds elapsed.')
