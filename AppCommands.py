from selenium import webdriver


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# Curret title of the web page
print(driver.title)

# current url of the page
print(driver.current_url)

# source of the page
print(driver.page_source)

driver.quit()