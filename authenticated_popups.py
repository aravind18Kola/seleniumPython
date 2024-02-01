from selenium import webdriver


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

# normal opening link
#driver.get("https://the-internet.herokuapp.com/basic_auth")

#open window with username password
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

