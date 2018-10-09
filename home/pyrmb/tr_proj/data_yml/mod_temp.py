#!/usr/bin/env python

from jinja2 import Template

wm_template=Template('''
name is a {{name}}
job - a {{job}}
''')
