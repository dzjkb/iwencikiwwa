#!/bin/bash

pip install jinja2-cli
jinja2 index.tmpl iwenciki.json --format=json >index.html