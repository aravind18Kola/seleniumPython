from selenium import webdriver

driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Total no of rows in table
rows = driver.find_elements_by_xpath("//table[@name='BookTable']//tr")
print(len(rows))


# Total no of columns in table
columns = driver.find_elements_by_xpath("//table[@name='BookTable']//tr[1]/th")
print(len(columns))


# Read specific row and column data
# 5th row and 1st column value
data = driver.find_element_by_xpath("//table[@name='BookTable']//tr[5]/td[1]").text
print(data)


# Read all the rows and columns data
for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data = driver.find_element_by_xpath("//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text
        print(data, end="   ")
    print()



# Read data based on the condition
# get the books name whose author is Mukesh
for r in range(2,len(rows)+1):
    author_name = driver.find_element_by_xpath("//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if author_name == 'Mukesh':
        bookname = driver.find_element_by_xpath("//table[@name='BookTable']//tr["+str(r)+"]/td[1]").text
        print(bookname)


driver.close()