import requests, os, bs4
os.makedirs('xkcd.com',exist_ok = True)
def main(start,end):
    print('downloading the %s...'%(url))
    res = requests.get(url)
    
