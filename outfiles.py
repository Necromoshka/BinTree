#!./venv/Scripts/python
# coding: utf-8
import os
sr_direktory = r'/mnt/share/'

for top, dirs, files in os.walk(sr_direktory):
    for nm in files:
        print nm


