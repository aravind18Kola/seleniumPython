from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='select2-billing_country-container']").click()
coutries_list = driver.find_elements_by_xpath("//ul[@id='select2-billing_country-results']/li")
print(len(coutries_list))

for country in coutries_list:
    if country.text == "India":
        country.click()
        break
