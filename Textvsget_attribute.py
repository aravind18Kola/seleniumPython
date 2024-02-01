from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://admin-demo.nopcommerce.com/")

email_box = driver.find_element_by_xpath("//*[@id='Email']")
email_box.clear()
email_box.send_keys("abcd@gmail.com")

# text
print(email_box.text)   # null
# get_attribute()
print(email_box.get_attribute('id'))   # abcd@gmail.com

# text
login_text = driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button")
print(login_text.text)   # LOG IN
