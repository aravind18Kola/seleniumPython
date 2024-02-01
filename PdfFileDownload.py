import os

from selenium import webdriver

loaction = os.getcwd()

def chromeSetup():
    preferences = {"download.default_directory":loaction, "plugins.always_open_pdf_externally":True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe",options=ops)
    return driver

driver = chromeSetup()
driver.get("https://file-examples.com/index.php/sample-documents-download/")
driver.maximize_window()
driver.find_element_by_xpath("//*[@id='page-top']/div[3]/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()
driver.find_element_by_xpath("//*[@id='table-files']/tbody/tr[1]/td[3]/a").click()