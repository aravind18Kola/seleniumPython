from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")

# explicit wait declaration
# mywait = WebDriverWait(driver, 10)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, Exception])

driver.get("https://www.google.com/")
driver.find_element_by_xpath("//*[@id='L2AGLb']/div").click()
driver.maximize_window()
search = driver.find_element_by_name('q')
search.send_keys("selenium")
search.submit()

# explicit wait usage
search_link = mywait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[12]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div[1]/div/div/span/a/h3")))
search_link.click()
driver.quit()
