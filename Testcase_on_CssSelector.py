# CSS selectos
# -----------------------------------
from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag & id combination
#driver.find_element_by_css_selector("input#email").send_keys("abc@gmail.com")

#tag & class combination
#driver.find_element_by_css_selector("input.inputtext").send_keys("xyz@gmail.com")

#tag & attribute combination
#driver.find_element_by_css_selector("input[data-testid=royal_email]").send_keys("abc@gmail.com")

#tag, class and attribute combination
driver.find_element_by_css_selector("input.inputtext[placeholder=Password]").send_keys("123456")