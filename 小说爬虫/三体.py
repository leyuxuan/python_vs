import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
x = 'http://www.shizongzui.cc/santi'
def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div',class_="bookcontent clearfix", id="BookText")
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    target = x
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', class_="booklist clearfix")
    chapters = chapters.find_all('a')
    y = '.txt'
    x = chapter_bs.find('h1')
    x = x.text
    book_name = x + y
    for chapter in tqdm(chapters,ncols = 50):
        chapter_name = chapter.string
        url = chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
'''
# 开64个线程池
pool = ThreadPool(64)
results = pool.map(downVideo, serach_res.keys())
pool.close()
pool.join()
'''
