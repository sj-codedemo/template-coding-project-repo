#!/usr/bin/env python

import datetime
import json

# Calculate the current year
current_year = datetime.datetime.now().year

# Read the existing cookiecutter.json
with open('cookiecutter.json', 'r') as file:
    data = json.load(file)

# Add or update the year in the data
data['current_year'] = current_year

# Write the updated data back to cookiecutter.json
with open('cookiecutter.json', 'w') as file:
    json.dump(data, file, indent=4)
