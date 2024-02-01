from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()

min_slider = driver.find_element_by_xpath("//*[@id='slider-range']/span[1]")
max_slider = driver.find_element_by_xpath("//*[@id='slider-range']/span[2]")

print("location of slider before moving")
print(min_slider.location)         # {'x': 59, 'y': 251}
print(max_slider.location)         # {'x': 510, 'y': 251}

act = ActionChains(driver)

act.drag_and_drop_by_offset(min_slider, 100, 0).perform()
act.drag_and_drop_by_offset(max_slider, -30, 0).perform()

print("location of slider after moving")
print(min_slider.location)
print(max_slider.location)