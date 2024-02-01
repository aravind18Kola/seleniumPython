from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element = driver.find_element_by_xpath("//*[@id='box6']")
target_element = driver.find_element_by_xpath("//*[@id='box106']")

act = ActionChains(driver)

act.drag_and_drop(source_element, target_element).perform()

source_element2 = driver.find_element_by_xpath("//*[@id='box3']")
target_element2 = driver.find_element_by_xpath("//*[@id='box103']")
act.drag_and_drop(source_element2, target_element2).perform()