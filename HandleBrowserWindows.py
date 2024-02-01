from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.selenium.dev/about/")
driver.maximize_window()

# Get current window id
# current_window_id = driver.current_window_handle
# print(current_window_id)

# Get multiple window ids
driver.find_element_by_xpath("//*[@id='announcement-banner']/div/div/div/h4/a").click()
multiple_window_ids = driver.window_handles
print(multiple_window_ids)

# switch to other window
driver.switch_to.window(multiple_window_ids[0])

