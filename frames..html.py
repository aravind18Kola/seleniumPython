from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()

#frame
driver.switch_to.frame("singleframe") # switching to frame
driver.find_element_by_xpath("/html/body/section/div/div/div/input").send_keys("HI")
driver.switch_to.default_content() # coming to main page or out of frame
driver.find_element_by_xpath("/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

#inner frame
outer_frame = driver.find_element_by_xpath("//*[@id='Multiple']/iframe")
driver.switch_to.frame(outer_frame)
inner_frame = driver.find_element_by_xpath("/html/body/section/div/div/iframe")
driver.switch_to.frame(inner_frame)
driver.find_element_by_xpath("/html/body/section/div/div/div/input").send_keys("Hello")

# Going to parent frame
driver.switch_to.parent_frame()
