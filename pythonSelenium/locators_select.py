import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, XPath, CSS Selector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# CSS Selector
# CSS  tagname[@attribute='value']
# CSS Searching by clases ex: .container .ng-pristine .form-group .form-control[name='name']
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Gilberto")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(1)
dropdown.select_by_visible_text("Male")
#dropdown.select_by_value()

# XPaths
#  //tagname[@attribute='value'] -> //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert ("Success" in message)

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain")
time.sleep(2)
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(2)
driver.close()
