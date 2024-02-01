import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://text-compare.com/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='ez-accept-all']").click()

input1 = driver.find_element_by_xpath("//*[@id='inputText1']")
input1.send_keys("Welcome")
input2 = driver.find_element_by_xpath("//*[@id='inputText2']")

act = ActionChains(driver)

# input1 ---- ctrl-A  select total text

# act.key_down(Keys.CONTROL)   # press the ctrl button
# act.send_keys("a")
# act.key_up(Keys.CONTROL)     # release the ctl button
# act.perform()

# OR

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input1  cntl- c      copy the text

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# navigate input box 2
input2.click()

# cntl - v       paste

act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

