import requests
import time
import os
from tqdm import tqdm
from bs4 import BeautifulSoup
from random import randint
path = os.getcwd()
def get_file():
    global book_name
    for i in os.listdir(path):
        if i == book_name:
            return True
        break
def get_book():
    url = 'http://www.kehuan.net.cn/book.html'
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text
    soup = BeautifulSoup(html, 'lxml')
    table_ = soup.table
    td_list = table_.find_all('td',class_ = 'tb')
    a_list = []
    for a in td_list:
        a_ = a.find_all('a')
        for d in a_:
            reeee = d.get('href')
            if not 'author' in reeee:
                a_list.append(reeee)
    return a_list

def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', class_='text')
    content = texts.text.strip().split('\xa0'*4)
    return content

for book_url in get_book():
    server = 'http://www.kehuan.net.cn/'
    target = 'http://www.kehuan.net.cn/' + str(book_url)
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', class_='book')
    chapters = chapters.find_all('a')
    x = chapter_bs.find('h1')
    x = x.text
    book_name = x + '.txt'
    if get_file():
        continue
    print('正在下载',book_name)
    for chapter in tqdm(chapters,ncols = 74):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
    time.sleep(randint(15,21))

