import time

from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# scroll down page by pixels
# driver.execute_script("window.scrollBy(0,3000)","") 
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels:", value)  # 3000

# scroll down page till the element is visible
# india_flag = driver.find_element_by_xpath("//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();",india_flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels:", value)

# scroll down till end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(5)

# scroll up to the starting the page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
