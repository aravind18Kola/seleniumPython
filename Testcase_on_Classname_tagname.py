# find the length of sliders
from selenium import webdriver


# Class Name
# -------------------
# will print total no of sliders on the page

# driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver.get("https://www.amazon.nl/ref=rhf_sign_in")
# sliders = driver.find_elements_by_class_name("a-carousel-card")
# print(sliders)
# print(len(sliders))


# Tag name
#----------------------------
# will print total no of links on the page
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
links = driver.find_elements_by_tag_name('a')
print(links)
print(len(links))
