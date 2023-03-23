"""
This script reads a JSON file and creates a list of all unique keys used in the JSON file.
Author: Robson Harrison
Date: March 2023
"""

import json

# Specify the path of the JSON file to read
filename = 'filepath'

# Open the file and load the JSON data
with open(filename) as f:
    data = json.load(f)

# Create a set to store the unique keys
keys = set()

# Define a function to recursively add keys to the set
def add_keys(d):
    if isinstance(d, dict):
        keys.update(d.keys())
        for v in d.values():
            add_keys(v)

# Loop through each item in the JSON data and add its keys to the set
if isinstance(data, dict):
    add_keys(data)
elif isinstance(data, list):
    for d in data:
        add_keys(d)

# Convert the set to a sorted list and print it
unique_keys = sorted(list(keys))
print("List of unique keys in the JSON file:")
print(sorted(list(keys)))
print(f"Total number of unique keys: {len(unique_keys)}")
