import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element_by_xpath("//*[@id='content']/div/ul/li[3]/button").click()
time.sleep(5)

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
#alertwindow.accept()    # perform click ok button action
alertwindow .dismiss()   # perform close action