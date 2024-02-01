from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='accept-choices']").click()
driver.switch_to.frame("iframeResult")

field1 = driver.find_element_by_xpath("//*[@id='field1']")
field1.clear()
field1.send_keys("Aravind")


button = driver.find_element_by_xpath("/html/body/button")

act = ActionChains(driver)
act.double_click(button).perform()