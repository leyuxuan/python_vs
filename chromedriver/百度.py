from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('user-agent="UCWEB7.0.2.37/28/999"')
driver = webdriver.Chrome('file\chromedriver.exe')
driver.get('https://www.baidu.com/')
