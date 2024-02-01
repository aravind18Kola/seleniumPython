from selenium import webdriver


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]").click()

# self
# text_msg = driver.find_element_by_xpath("//a[contains(text(),'Linde India')]/self::a").text
# print(text_msg)

# parent
# parent_name = driver.find_element_by_xpath("//a[contains(text(),'Linde India')]/parent::td").text
# print(parent_name)

#child
# childs = driver.find_elements_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr/child::td")
# print(len(childs))

#Ancestor
txt_msg1=driver.find_element_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr").text
print(txt_msg1)

# descendent
descendants = driver.find_elements_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr/descendant::*")
print(len(descendants))

# Following
followings = driver.find_elements_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr/following::*")
print(len(followings))

# Following-sibling
following_siblings = driver.find_elements_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr/following-sibling::*")
print(len(following_siblings))

# preceding
precedings = driver.find_elements_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr/preceding::*")
print(len(precedings))

# preceding-sibling
preceding_siblings = driver.find_elements_by_xpath("//a[contains(text(),'Linde India')]/ancestor::tr/preceding-sibling::*")
print(len(preceding_siblings))

driver.close()
