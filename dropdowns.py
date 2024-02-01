from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

drp_country_ele = Select(driver.find_elements_by_xpath("//*[@id='input-country']"))


# select option from the dropdown
drp_country_ele.select_by_visible_text("India")   # india
# drp_country.select_by_value('44')  # china
# drp_country_ele.select_by_index(2)

# capture all the options and print down
all_options = drp_country_ele.options
print(len(all_options))

# for opt in all_options:
#     print(opt.text)

# select option without built-in method
for opt in all_options:
    if opt.text == 'India':
        opt.click()
        break
