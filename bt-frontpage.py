#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import requests, sys, time, json, collections
from bs4 import BeautifulSoup
import mysql.connector


def main():
    position = 0
                
    r = requests.get('http://www.bt.no')
    soup = BeautifulSoup(r.text, 'html.parser')

    for row in soup.findAll('div', { 'class' : 'df-article-content' }):
        position += 1

        try:
            title = row.h3.get_text().strip().encode('utf-8')
            print(position)
            print(title)
        except AttributeError:
            pass

        
if __name__ == '__main__':
    sys.exit(main(*sys.argv[1:]))