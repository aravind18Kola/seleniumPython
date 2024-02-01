from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")

act = ActionChains(driver)

act.context_click(button).perform()