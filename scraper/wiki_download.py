import requests
import bz2
import subprocess

# Library for parsing HTML/XML
from bs4 import BeautifulSoup

import sys
from keras.utils import get_file
import os

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

print(f'There are {len(file_info)} partitions.')

data_path = data_paths[-1]
print(data_path)
lines = []

for i, line in enumerate(subprocess.Popen(['bzcat'],
                         stdin = open(data_path),
                         stdout = subprocess.PIPE).stdout):
    lines.append(line)
    if i > 5e5:
        break

print(lines[-165:-109])
