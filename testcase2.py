#              Testcase 2
# -----------------------------------------------------------------
#  open web browser(chrome/firefox/edge)
#  open URL https://admin-demo.nopcommerce.com/login
#  provide email  (admin@yourstore.com)
#  click on login
#  capture title of the dashboard page (actual title)
#  verify title of the page: " Dashboard / nopcommerce administration" (Expected)
#  close browser


from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Password").send_keys("admin")
driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
actual_title = driver.title
# print(actual_title)
expected_title = "Dashboard / nopCommerce administration"
if actual_title == expected_title:
    print("Testcases passed")
else:
    print("Testcase failed")
