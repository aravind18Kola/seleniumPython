#       Testcase

# Open web browser (chrome/firefox/web)
# open url https://opensource-demo.orangehrmlive.com/
# enter username (Admin).
# enter password (admin123)
# click on login
# capture title of the homepage (Actual title)
# verify title of the page : OrangeHRM  (Expected)
# close browser

from selenium import webdriver
driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.nl/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Feu.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3Dsgx4Qle5QjP6VNFneXns1pEhSbjJ3UY9IanJAvsqlHKCxAAAAAQAAAABlqWDhcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Foffers%2Fnonprimehomepage%3Fref_%253Ddv_web_force_root&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_nl&openid.mode=checkid_setup&siteState=261-3379451-9788325&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.find_element_by_name("email").send_keys("6281098360")
driver.find_element_by_id("continue").click()
driver.find_element_by_name("password").send_keys("aravind05")
driver.find_element_by_id("signInSubmit").click()

