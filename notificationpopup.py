from selenium import webdriver

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe", options=ops)
driver.get("https://whatmylocation.com/")