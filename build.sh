#!/bin/bash

pip install jinja2-cli
jinja2-cli index.tmpl iwenciki.json --format=json >index.html