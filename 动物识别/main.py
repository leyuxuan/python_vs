# encoding:utf-8
import sys
import requests
import base64
import json
API_KEY =  'LHWvA7bXWVM4iGH3SrT4SyoL'
SECRET_KEY = 'Nv7OLR4ToTR40puzpSBGb7hQgzOAkwUH'
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()


    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"

x = fetch_token()
# 二进制方式打开图片文件
f = open('text.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = x
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    #print (response.json())
    x = response.json()['result']
    y = len(x)
    jsons=json.loads(response.text)
    for i in jsons['result']:
        sr = i['score']
        sr = str(sr)
        print('相似度:' + i['score'])
        print('名称:' + i['name'])
        print('')

