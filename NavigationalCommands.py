from selenium import webdriver


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.snapdeal.com/")  # opens snap deal page
driver.get("https://www.amazon.com/")  # in the same tab opens amazon tab

# back
driver.back()      # go back to snap deal page

# forward
driver.forward()   # go forward to amazon page

# refresh
driver.refresh()    # it refreshes the page
