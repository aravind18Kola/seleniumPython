from selenium import webdriver
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")


#Absolute or full Xpath
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()


#Relative or partial Xpath
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='small-searchterms']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element_by_xpath("//*[@id='small-search-box-form']/button").click()

# OR
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("//input[@id='small-searchterms' or @name='qq']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element_by_xpath("//button[@class='button-1 search-box-button' or type='submit1'] ").click()

# AND
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("//input[@id='small-searchterms' and @name='q']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# contains() & starts_with()
# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element_by_xpath("//input[contains(@id,'small')]").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element_by_xpath("//button[starts-with(@class,'button-1 search')]").click()

# text()
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.find_element_by_xpath("//a[text()='Forgot password?']").click()