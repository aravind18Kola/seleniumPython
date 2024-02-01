from selenium import webdriver


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

# is_displayed() , is_enabled()
search_box = driver.find_element_by_xpath("//input[@id='small-searchterms']")
print("display status  :  ", search_box.is_displayed())
print("enabled status  :  ", search_box.is_enabled())

# is_selected()     for radio buttons and checkboxes
male_rb = driver.find_element_by_xpath("//input[@id='gender-male']")
female_rb = driver.find_element_by_xpath("//input[@id='gender-female']")
print(male_rb.is_selected())
print(female_rb.is_selected())

male_rb.click()

print("After selecting the male radio button")
print(male_rb.is_selected())
print(female_rb.is_selected())

driver.close()