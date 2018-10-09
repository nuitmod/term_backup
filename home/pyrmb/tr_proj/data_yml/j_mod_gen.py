#!/usr/bin/env python

import yaml, time
from mod_temp import wm_template

wmns = yaml.load(open('mod_info.yml'))

#def f_out():
for wm in wmns:
    w1_conf=wm['name']+'_dat.txt'
    with open(w1_conf, 'w') as f:
        f.write(wm_template.render(wm))

#f_out()
