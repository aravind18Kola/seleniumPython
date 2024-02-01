from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)  # switch to frame

# mm/dd/yyyy
#driver.find_element_by_id('datepicker').send_keys("02/19/2000")

# or

year = "2025"
month = "April"
day = "19"
driver.find_element_by_xpath("//*[@id='datepicker']").click()
# selecting month and year
while True:
    m = driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text
    y = driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text
    if m == month and y == year:
        break
    else:
        driver.find_element_by_xpath("//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # next arrow


# selecting date
dates = driver.find_elements_by_xpath("//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dt in dates:
    if dt.text == day:
        dt.click()
        break

# if you want  to select previour year just change the next arrow with previous arrow web element

