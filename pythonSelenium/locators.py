import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, XPath, CSS Selector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS Selector
# CSS  tagname[@attribute='value']
# CSS Searching by clases ex: .container .ng-pristine .form-group .form-control[name='name']
driver.find_element(By.CSS_SELECTOR, "input[name='name']")

# XPaths
#  //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert ("Success" in message)

time.sleep(2)
driver.close()


