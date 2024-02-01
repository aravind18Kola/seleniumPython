from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.foundit.in/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='heroSection-container']/div[3]/div[2]/div[2]").click()
driver.find_element_by_xpath("//*[@id='file-upload']").send_keys("C:/Users/arkola\Downloads\Secure_Network_Analytics_testcases_Arvind.docx")
driver.find_element_by_xpath("//*[@id='pop_upload']").click()