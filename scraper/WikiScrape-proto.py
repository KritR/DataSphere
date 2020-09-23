import requests 
import xml.sax
import mwparserfromhell
import subprocess
import os
#from timer import Timer
import time
import threading
from tqdm import tqdm

#data_path = 'C:\\Users\\sambr\\Downloads\\enwiki-20190101-pages-articles-multistream.xml.bz2'
#data_path = os.path.join("Users", "sambr", "Downloads", "enwiki-20190101-pages-articles-multistream.xml.bz2")

data_path = '.\\enwiki-20190101-pages-articles-multistream.xml'

class WikiXmlHandler(xml.sax.handler.ContentHandler):
    """Content handler for Wiki XML data using SAX"""
    def __init__(self):
        xml.sax.handler.ContentHandler.__init__(self)
        self._buffer = None
        self._values = {}
        self._current_tag = None
        self._pages = []
        self._article_count = 0
        self._events = None

    def characters(self, content):
        """Characters between opening and closing tags"""
        if self._current_tag:
            self._buffer.append(content)

    def startElement(self, name, attrs):
        """Opening tag of element"""
        if name in ('title', 'text'):
            self._current_tag = name
            self._buffer = []

    def endElement(self, name):
        """Closing tag of element"""
        if name == self._current_tag:
            self._values[name] = ' '.join(self._buffer)

        if name == 'page':
            #self._pages.append((self._values['title'], self._values['text']))
            self._article_count += 1
            #Send the page to the process article function
            event = process_article(**self._values, template = 'Infobox event')

            if event:
                self._events.append(event)

def process_article(title, text, template = 'Infobox event'):
    """Process a wikipedia article looking for template"""

    #Create a parsing object
    wikicode = mwparserfromhell.parse(text)

    #Search through templates for the template
    matches = wikicode.filter_templates(matches = template)

    if len(matches) >= 1:
        # Extract information from infobox
        properties = {param.name.strip_code().strip(): param.value.strip_code().strip()
                       for param in matches[0].params
                       if param.value.strip_code().strip()}

        return (title, properties)


# Object for handling xml
handler = WikiXmlHandler()# Parsing object
parser = xml.sax.make_parser()
parser.setContentHandler(handler)# Iteratively process file
start = time.time()
with open(data_path, encoding="utf8") as fp:
    for line in tqdm(fp):

        try:
        #Process Line
            parser.feed(line)
            #if len(handler._pages) > 0:
             #   print("FOUND A NEW PAGE")
            # Stop when 3 articles have been found
            #if len(handler._pages) > 2:
              #  break
        except StopIteration:
            break

        

end = time.time()
events = handler._events

print(f'\nSearched through {handler._article_count} articles.')
print(f'\nFound {len(events)} events in {round(end - start)} seconds.')