import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

from DataDrivenTesting import ExcelUtils
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\Sampless\data.xlsx"

rows = ExcelUtils.getRowCount(file,"Sheet1")
for r in range(2, rows+1):
    # reading data from excel
    principle = ExcelUtils.readData(file,"Sheet1",r,1)
    Roi = ExcelUtils.readData(file,"Sheet1",r,2)
    period1 = ExcelUtils.readData(file,"Sheet1",r,3)
    period2 = ExcelUtils.readData(file,"Sheet1",r,4)
    frequency = ExcelUtils.readData(file,"Sheet1",r,5)
    expected_maturity_value = ExcelUtils.readData(file,"Sheet1",r,6)
    # passing data to the application
    driver.find_element_by_xpath("//*[@id='principal']").send_keys(principle)
    driver.find_element_by_xpath("//*[@id='interest']").send_keys(Roi)
    driver.find_element_by_xpath("//*[@id='tenure']").send_keys(period1)
    period2_dropdown = Select(driver.find_element_by_xpath("//*[@id='tenurePeriod']"))
    period2_dropdown.select_by_visible_text(period2)
    driver.find_element_by_xpath("//*[@id='frequency']").send_keys(frequency)
    frequency_dropdown = Select(driver.find_element_by_xpath("//*[@id='frequency']"))
    frequency_dropdown.select_by_visible_text(frequency)
    driver.find_element_by_xpath("//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    actual_maturity_value = driver.find_element_by_xpath("//span[@id='resp_matval']/strong").text
    if float(expected_maturity_value) == float(actual_maturity_value):
        print("test passed")
        ExcelUtils.writeData(file,"Sheet1",r,8,"Passed")
        ExcelUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        ExcelUtils.writeData(file, "Sheet1", r, 8, "failed")
        ExcelUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element_by_xpath("//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)

driver.close()

