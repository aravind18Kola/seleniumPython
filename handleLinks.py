from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.find_element_by_link_text("Digital downloads").click()  #link_text
# driver.find_element_by_partial_link_text("Digital").click()  # partial_link_text


# find the number of links
links = driver.find_elements_by_tag_name("a")
print(len(links))

