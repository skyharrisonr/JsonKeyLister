"""
This script reads a JSON file and creates a list of all unique keys used in the JSON file.
Author: Robson Harrison
Date: March 2023
"""

import json

# Specify the path of the JSON file to read
filename = 'example.json'

# Open the file and load the JSON data
with open(filename) as f:
    data = json.load(f)

# Create a set to store the unique keys
keys = set()

# Loop through each dictionary in the JSON data and add its keys to the set
for d in data:
    if isinstance(d, dict):
        keys.update(d.keys())

# Convert the set to a sorted list and print it
print("List of unique keys in the JSON file:")
print(sorted(list(keys)))
