from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

# implicit_wait
driver.implicitly_wait(10)  # applicable for all below statements

driver.get("https://www.google.com/")
driver.find_element_by_xpath("//*[@id='L2AGLb']/div").click()
driver.maximize_window()
search = driver.find_element_by_name('q')
search.send_keys("selenium")
search.submit()
driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div/div/div[1]/div/div/span/a/h3").click()

driver.quit()