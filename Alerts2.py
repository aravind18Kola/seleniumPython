
from selenium import webdriver


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://mypage.rediff.com/")
driver.maximize_window()

driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/table/tbody/tr[1]/td[3]/input").click()

alertbox = driver.switch_to.alert
alertbox.accept()
