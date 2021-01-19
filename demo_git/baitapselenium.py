from selenium import webdriver

driver =  webdriver.Chrome("D:\\webdriver\\chromedriver.exe")
driver.get("http://45.79.43.178/source_carts/wordpress/wp-login.php")

username = driver.find_element_by_id("user_login")
username.send_keys("admin")
password = driver.find_element_by_id("user_pass")
password.send_keys("123456aA")

form = driver.find_element_by_id("loginform")
form.submit()

name = driver.find_element_by_xpath("//div[@class='quicklinks']//li[@id='wp-admin-bar-my-account']//a").text
print("Username :", name)