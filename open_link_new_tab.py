from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()

# driver.get("https://demo.nopcommerce.com/")
# reglisnk = Keys.CONTROL+Keys.RETURN
# driver.find_element_by_xpath("/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a").send_keys(reglisnk)


# New tab  ---selenium 4   open the new tab and awitch to that tab

# driver.get("https://www.opencart.com")
# driver.switch_to.new_window('tab')      # will work in selenium 4
# driver.get("https://facebook.com")


# New tab  ---selenium 4   open the new window and awitch to that tab

driver.get("https://www.opencart.com")
driver.switch_to.new_window('window')   # will work in selenium 4
driver.get("https://facebook.com")