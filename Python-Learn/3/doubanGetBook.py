import requests
from bs4 import BeautifulSoup
import re

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8  so

home = 'https://book.douban.com/'
url = 'https://book.douban.com/tag/?view=type&icn=index-sorttags-all'

resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')

#print(soup.prettify())


# 找到 文化 这个大类！
# category = soup.find_all(name='a', attrs={'name':'文化'})

def specific_name(tag):
    return tag.has_attr('name') and tag.get('name') == '文化'

category = soup.find(specific_name)

for e in category.next_siblings:
    print(e)


def has_href(tag):
    return tag.has_attr('href')

sub_category = {}

for e in category.next_siblings:
    if e == '\n':
        pass
    else:
        for a in e.find_all(has_href):
            sub_category[a.get_text()] = home + a.get('href')


def get_soup(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    return soup

soup = get_soup(sub_category['中国历史'])

books = {}
for ul in soup.select('ul[class="subject-list"]'):
    for li in ul.select('li[class="subject-item"]'):
        for div in li.select('div[class="info"]'):
            books[div.h2.a.get('title')] = div.h2.a.get('href')

for ul in soup.select('ul[class="subject-list"]'):
    for div in ul.select('div[class="info"]'):
        books[div.h2.a.get('title')] = div.h2.a.get('href')

for div in ul.select('div[class="info"]'):
    books[div.h2.a.get('title')] = div.h2.a.get('href')

for h2 in soup.select('h2[class=""]'):
    books[h2.a.get('title')] = h2.a.get('href')


def has_href_title(tag):
    return tag.has_attr('href') and tag.has_attr('title')

for a in soup.find_all(has_href_title):
    if a == '\n':
        pass
    else:
        books[a.get('title')] = a.get('href')

soup = get_soup(books['万历十五年'])

instro = {}
instro['万历十五年'] = soup.select('div[class="intro"]')[0].text.strip()


# 写出
def write_text():
    with open('d:/kk/{}-{}.txt'.format('历史', '万历十五年'), 'w', encoding='utf-8') as f:
        f.write(instro['万历十五年'])

write_text()