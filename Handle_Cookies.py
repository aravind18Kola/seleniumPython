from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies = driver.get_cookies()
# print(len(cookies))

# print details of all cookies
# for cookie in cookies:
#     #print(cookie)
#     print(cookie.get('name'), ":", cookie.get('value'))

# Add a new cookie to the browser
driver.add_cookie({"name":'myCookie','value':'123567'})
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie.get('name'), ":", cookie.get('value'))


# delete specific cookie from the browser
driver.delete_cookie("myCookie")
print("After deleted 1")
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie.get('name'), ":", cookie.get('value'))


# delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("affter deleting all",len(cookies))

driver.quit()