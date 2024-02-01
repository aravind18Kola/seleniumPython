from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element_by_id('dob').click()

month = Select(driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[1]/div/select[1]"))
month.select_by_visible_text("Feb")
year = Select(driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div[1]/div/select[2]"))
year.select_by_visible_text("2000")

dates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dt in dates:
    if dt.text == "19":
        dt.click()
        break
