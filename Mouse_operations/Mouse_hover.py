from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
computers = driver.find_element_by_xpath("/html/body/div[6]/div[2]/ul[1]/li[1]/a")
desktops = driver.find_element_by_xpath("/html/body/div[6]/div[2]/ul[1]/li[1]/ul/li[1]/a")

act = ActionChains(driver)
act.move_to_element(computers).move_to_element(desktops).click().perform()
