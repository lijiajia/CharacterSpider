#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import re
from BeautifulSoup import BeautifulSoup


BASE_DIR = 'http://tool.httpcn.com'


def get_character(url):
    path = BASE_DIR + url
    html = urllib2.urlopen(path).read().decode('utf-8')
    print '============================================================'
    print html
    print '============================================================'
    soup = BeautifulSoup(html)
    character_list = soup.findAll(href=re.compile('^/Html/KangXi/*'))
    for character in character_list:
        print character


def main():
    html = urllib2.urlopen('http://tool.httpcn.com/KangXi/BuShou.html').read()
    print html
    soup = BeautifulSoup(html)
    bushou_list = soup.findAll(href=re.compile('^/Html/KangXi/*'))
    for bushou in bushou_list:
        href = bushou['href']
        get_character(href)
        return 0


if __name__ == '__main__':
    main()
