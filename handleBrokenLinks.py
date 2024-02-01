# we need to install requests module in interpreter
import requests
from requests import request
from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

links = driver.find_elements_by_tag_name('a')
count = 0
for link in links:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url, "is broken link")
        count+=1
    else:
        print(url, "is valid link")
print("total broken links : ", count)
