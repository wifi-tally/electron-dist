#!/usr/bin/env python3

# Sets version of vtally

import json
import os
import logging
import pathlib

basedir = pathlib.Path(os.path.dirname(os.path.dirname(__file__)))

with open(basedir / "package.json") as json_file:
    package = json.load(json_file)

package['dependencies']['vtally'] = os.getenv("VTALLY_SOURCE")

with open(basedir / "package.json", 'w') as outfile:
    json.dump(package, outfile, indent=2)

logging.info("package.json updated")

