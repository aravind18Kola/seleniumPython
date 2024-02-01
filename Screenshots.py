import os

from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.save_screenshot(os.getcwd()+"/abcd.png")


# driver.get_screenshot_as_file()
# driver.get_screenshot_as_base64()
# driver.get_screenshot_as_png()


driver.quit()