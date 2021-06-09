from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
browser = webdriver.Ie()
browser.maximize_window()
browser.get('https://mail.aliyun.com')
time.sleep(1)
browser.find_element_by_xpath('//*[@id="fm-login-id"]').send_keys('leyuxuan1230')
browser.find_element_by_xpath('/html/body/div[1]/form/div[3]/dl[2]/dd/div/input').send_keys('leyuxuan1230').submit()
