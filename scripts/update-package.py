#!/usr/bin/env python3

# Updates package.json with meta information from vtally in node_modules/

import json
import os
import logging

basedir = os.path.dirname(os.path.dirname(__file__))

with open(f'{basedir}/node_modules/vtally/package.json') as json_file:
    vtally = json.load(json_file)

with open(f'{basedir}/package.json') as json_file:
    ours = json.load(json_file)

ours['version'] = vtally['version']
ours['description'] = vtally['description']
ours['keywords'] = vtally['keywords']
ours['homepage'] = vtally['homepage']
ours['bugs'] = vtally['bugs']

with open(f'{basedir}/package.json', 'w') as outfile:
    json.dump(ours, outfile, indent=2)

logging.info("package.json updated")

