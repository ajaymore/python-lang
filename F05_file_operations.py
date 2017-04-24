__author__ = 'Mystique'

# Open file for reading
f = open('read_file.json', 'r')
f_json = open('read_file.json', 'r')
f1 = open('newFile.txt', 'w')
# Other modes:
# r+ - read write
# a - append
# w - write only
# methods to call : f.read(), readline()

for line in f:
    print(line, end='')
print()
value = ('the answer', 42)
f1.write(str(value))

import json

print(json.dumps([1, 'simple', 'list']))
jsonList = json.load(f_json)
print(jsonList[0]['name'])

import os

print()
files = [f for f in os.listdir('.') if os.path.isdir(f)]
subPackFiles = [[f1 for f1 in os.listdir(f)] for f in files if not f.startswith('.') | f.startswith('_')]
print(files)
print(subPackFiles)