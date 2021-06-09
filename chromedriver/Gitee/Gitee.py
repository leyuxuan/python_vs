from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
url = input('url?')
name = input('name?')
browser = webdriver.Edge()
browser.maximize_window()
time.sleep(1.1)
browser.get('https://gitee.com/login')
userElem = browser.find_element_by_id('user_login')
userElem.send_keys('leyuxuan')
passwordElem = browser.find_element_by_id('user_password')
passwordElem.send_keys('leyuxuan1230')
passwordElem.submit()
time.sleep(5)
browser.find_element_by_xpath('/html/body/div[2]/header/div/div/div[7]/div[2]/i').click()
time.sleep(3)
browser.find_element_by_xpath('/html/body/div[2]/header/div/div/div[7]/div[2]/div/a[5]').click()
time.sleep(2)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[2]/div/div[1]/input').send_keys(url)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[6]/div/div[1]/input').send_keys(name)
time.sleep(0.5)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[10]/div[1]/div/label').click()
time.sleep(0.8)
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/form/div[13]/input').click()
time.sleep(4)
d_url = str(browser.current_url) + '/repository/archive/master.zip'
browser.quit()
time.sleep(10)
os.system('wget ' + d_url)
t = input('是否成功？(y,n)')
if t == 'y':
    sys.quit()
else:
    time.sleep(5)
    os.system('wget ' + d_url)
