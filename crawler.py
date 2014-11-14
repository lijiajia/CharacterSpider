#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
import re
from BeautifulSoup import BeautifulSoup


BASE_DIR = 'http://tool.httpcn.com'


def convert_to_standard_html(html):
    html = html.replace(u'点击显示注释', u'"点击显示注释"')
    html = html.replace('href=', 'href="')
    html = html.replace('.shtml', '.shtml"')
    return html


def process_to_database(ch, url):
    spelling_list = []
    symbol = 0
    hk_spelling = ''
    cangjie_code = ''

    path = BASE_DIR + url
    html = urllib2.urlopen(path).read()
    soup = BeautifulSoup(html)
    content_m = soup.find('div', {'class': 'content_m'})
    if content_m is None:
        return None
    content = content_m.find('div', {'id': 'div_a1'})

    pinyin_table = content.find('table')
    pinyin_module = pinyin_table.find('span', {'class': 'pinyin'})
    pinyin_script_list = pinyin_module.findAll('script')
    for pinyin_script in pinyin_script_list:
        pinyin = pinyin_script.text
        s_index = pinyin.find('/')
        length = len(pinyin)
        if re.match('^\d$', pinyin[length - 3]):
            length -= 1
        spelling_list.append(pinyin[s_index + 1: length - 2])

    code_module = content.find('p', {'class': 'text16'})
    cangjie_code = code_module('span')[2].nextSibling.strip()

    content_module_list = content.findAll('div', {'class': 'text16'})
    for content_module in content_module_list:
        name = content_module.find('span', {'class': 'zi18b'})
        if name is not None:
            if name.string.find(u'字形结构') >= 0:
                symbol_list = content_module.findAll('span', {'class': 'b'})
                for symbol_obj in symbol_list:
                    if symbol_obj.string.find(u'笔顺编号') >= 0:
                        symbol = int(symbol_obj.nextSibling.string[3])
                        break
            elif name.string.find(u'音韵参考') >= 0:
                hk_spelling_list = content_module.findAll('span', {'class': 'b'})
                for hk_spelling_obj in hk_spelling_list:
                    if hk_spelling_obj.string.find(u'粤') >= 0:
                        hk_spelling = hk_spelling_obj.nextSibling.string[3:]
                        break
                length = len(hk_spelling)
                hk_spelling = hk_spelling if len(hk_spelling) <= 0 or not re.match('^\d$', hk_spelling[length - 1]) else hk_spelling[:-1]

    ret = {
        'character': ch,
        'spelling': spelling_list,
        'symbol': symbol,
        'cangjie': cangjie_code,
        'hk_spelling': hk_spelling
    }
    print ret
    return ret


def get_character_html(url):
    path = BASE_DIR + url
    html = urllib2.urlopen(path).read()
    html = convert_to_standard_html(html)
    soup = BeautifulSoup(html)
    character_list = soup.findAll(href=re.compile('^/Html/KangXi/*'))
    for character in character_list:
        process_to_database(character.text, character['href'])


def main():
    html = urllib2.urlopen('http://tool.httpcn.com/KangXi/BuShou.html').read()
    soup = BeautifulSoup(html)
    bushou_list = soup.findAll(href=re.compile('^/Html/KangXi/*'))
    for bushou in bushou_list:
        href = bushou['href']
        get_character_html(href)


if __name__ == '__main__':
    main()
