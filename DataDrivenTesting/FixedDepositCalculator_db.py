import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import mysql.connector

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

try:
    con = mysql.connector.connect(host="localhost", port=3306, user="root",password="root",



                                  database="mydb")
    curs = con.cursor()
    curs.execute("select * from caldata")
    for row in curs:
        principle = row[0]
        Roi = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        expected_maturity_value = row[5]
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
        else:
            print("test failed")

        driver.find_element_by_xpath("//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(2)
    con.close()
except:
    print("connection unsuccessful....")
driver.close()



