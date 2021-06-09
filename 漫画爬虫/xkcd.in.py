import requests, os, bs4
from time import sleep
url = 'https://xkcd.in/'
os.makedirs('xkcd',exist_ok = True)
print('downloading the %s...'%(url))
res = requests.get(url)
res.encoding = 'utf-8'
res.raise_for_status()   # 返回请求的状态
soup = bs4.BeautifulSoup(res.text,'html.parser')
comicele = soup.find('div',class_ = "comic-body")
comicele = comicele.find('img')
if comicele == []:
    print('could not find comic image')
else:
    comicurl = 'https://xkcd.in/' + comicele.get('src')
    res = requests.get(comicurl)

with open(".\\xkcd\\%s.png"%(soup.find('div',class_="content_first").find('h1').text.replace(' ',"").replace('\r\n',"")),'wb') as f:
    f.write(res.content)
url = 'https://xkcd.in/comic?lg=cn&id=2384'
def main():
    global soup
    global url
    while True:
        print('downloading the %s...'%(url))
        res = requests.get(url)
        res.encoding = 'utf-8'
        if '<h1>桶 - 1</h1>' in res:
            soup = bs4.BeautifulSoup(res.text,'html.parser')
            comicele = soup.find('div',class_ = "comic-body")
            comicele = comicele.find('img')
            if comicele == []:
                print('could not find comic image')
            else:
                comicurl = 'https://xkcd.in/' + comicele.get('src')
                res = requests.get(comicurl)

            with open(".\\xkcd\\%s.png"%(soup.find('div',id="content").find('h1').text.replace(' ',"").replace('\r\n',"")),'wb') as f:
                f.write(res.content)
            break
        soup = bs4.BeautifulSoup(res.text,'html.parser')
        comicele = soup.find('div',class_ = "comic-body")
        comicele = comicele.find('img')
        if comicele == []:
            print('could not find comic image')
        else:
            comicurl = 'https://xkcd.in/' + comicele.get('src')
            res = requests.get(comicurl)

        with open(".\\xkcd\\%s.png"%(soup.find('div',id="content").find('h1').text.replace(' ',"").replace('\r\n',"")),'wb') as f:
            f.write(res.content)
        try:
            print(url)
            url = 'https://xkcd.in/' + soup.find('div',class_ = "nextLink").find('a').get('href')
        except expression as e:
            print(e)
            input()
        sleep(3)   #不加这个你知道的


sleep(2) #不加这个你知道的
try:
    main()
except:
    sleep(1)
    main()

