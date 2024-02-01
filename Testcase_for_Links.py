#  Link text & partial link text
# ---------------------------------------------------------------------------

from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
#Link text
driver.find_element_by_link_text("Log in").click()

#partial link text
driver.find_element_by_partial_link_text("Forgot").click()