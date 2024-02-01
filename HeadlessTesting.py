from selenium import webdriver


def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.headless = True
    driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe", options=ops)
    return driver


driver = headless_chrome()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
