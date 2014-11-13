#!/usr/bin/env python
# coding=utf-8

import urllib2
from BeautifulSoup import BeautifulSoup


def main():
    html = urllib2.urlopen('http://tool.httpcn.com/KangXi/BuShou.html').read()
    print html
    soup = BeautifulSoup(html)
    title = soup.title
    print type(title)
    print title.name
    print title.string
#    print soup.find_all('a')


if __name__ == '__main__':
    main()
