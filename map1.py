#!/usr/bin/env python3

import sys
import os
import urllib.parse


def check(codep, namep):
    if codep != 'en':
        return False

    if namep.split(':')[0] in filter_out_words or namep[0].islower():
        return False

    if '.' in namep and namep.split('.')[-1] in filter_out_files:
        return False

    if namep in filter_out_pages:
        return False
    return True


filter_out_words = ['Media', 'Special', 'Talk', 'User', 'User_talk',
                    'Project', 'Project_talk', 'File', 'File_talk',
                    'MediaWiki', 'MediaWiki_talk', 'Template',
                    'Template_talk', 'Help', 'Help_talk', 'Category',
                    'Category_talk', 'Portal', 'Wikipedia', 'Wikipedia_talk']

filter_out_files = ['jpg', 'gif', 'png', 'JPG', 'GIF', 'PNG', 'ico', 'txt']

filter_out_pages = ['404_error', 'Main_Page', 'Hypertext_Transfer_Protocol',
                    'Favicon.ico', 'Search']

filepath = os.environ.get("map_input_file", "stdin")
date = os.path.split(filepath)[-1].split('-')[1]

for line in sys.stdin:
    [code, name, views, *args] = line.strip().split()
    name = urllib.parse.unquote_plus(name)

    if check(code, name):
        print(date + "}" + name + "}" + views)
    else:
        continue
