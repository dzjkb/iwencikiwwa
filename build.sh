#!/bin/bash

pip install jinja2-cli pandas
python parse_csv.py
jinja2 index.tmpl iwenciki.json --format=json >index.html