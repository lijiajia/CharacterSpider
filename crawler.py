#!/usr/bin/env python
# coding=utf-8

import urllib2


def main():
    html = urllib2.urlopen('http://baidu.com').read()
    print html


if __name__ == '__main__':
    main()
