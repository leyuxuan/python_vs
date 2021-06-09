import requests as r
from bs4 import *
from wordcloud import *
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'
}
res = r.get('http://finance.people.com.cn',headers = headers)
res.encoding = 'GB2312'
soup = BeautifulSoup(res.text,'html.parser')

print(soup.find('div',class_="page_n clearfix"))
pages_num = int(len(soup.find('div',class_="page_n clearfix").find_all('a')))

def bl(list):
    rr = ''
    for d in list:
        if '此外' in d or '同时' in d:
            pass
        else:
            rr += str(d) + '\n'
    return rr
new_url_list2 = []
item = 1
for i in range(7):
    soup = BeautifulSoup(res.text,'html.parser')
    new_url_list3 = []
    res = r.get('http://scitech.people.com.cn/index%s.html'%(item),headers = headers)
    res.encoding = 'GB2312'
    soup = BeautifulSoup(res.text,'html.parser')
    new_url_list = soup.find_all('div',class_='on')
    for x in new_url_list:
        new_url_list3.append('http://scitech.people.com.cn'+x.find('a').get('href'))
    new_url_list2 += new_url_list3
    item += 1
url_list = new_url_list2
text = []
for url in url_list:
    try:
        res = r.get(url,headers = headers)
    except:
        pass
    res.encoding = 'GB2312'
    soup = BeautifulSoup(res.text,'html.parser')
    print(bl(soup.h1))
    rde = soup.find('div',class_="rm_txt_con cf").find_all('p')
    for defg in rde:
        text.append(defg.text)

w = WordCloud(background_color='black', font_path='./ziti.ttf', width=970, height=760)
w.generate(bl(text))
w.to_file('wordcloud.png')
