import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
time.sleep(5)
driver.find_element(By.NAME, "password").send_keys("admin321")
time.sleep(5)
invalidCred = driver.find_element(By.XPATH,"//div[@class='oxd-alert oxd-alert--error']/div/p").text
assert invalidCred=="Invalid credentials"
print("test case Failed")
