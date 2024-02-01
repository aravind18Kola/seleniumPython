from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#selecting checkbox
#driver.find_element_by_xpath("//*[@id='sunday']").click()

# selecting al the checkboxes
# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'day')]")
# for cb in checkboxes:
#     cb.click()


# selecting multiple checkboxes
# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'day')]")
# for cb in checkboxes:
#     weekname = cb.get_attribute('id')
#     if weekname == 'monday' or weekname == 'wednesday':
#         cb.click()


# select last two checkboxes
# checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'day')]")
# leng = len(checkboxes)
# for i in range(leng-2,leng):
#     checkboxes[i].click()


# select first two check boxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'day')]")
leng = len(checkboxes)
for i in range(0, 2):
    checkboxes[i].click()


# for clearing all the check boxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox' and contains(@id,'day')]")
for cb in checkboxes:
    if cb.is_selected():
        cb.click()