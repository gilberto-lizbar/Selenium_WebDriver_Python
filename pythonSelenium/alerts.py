import time

from selenium import webdriver
from selenium.webdriver.common.by import By

name = "Gilberto"

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# Switch to Alert
alert = driver.switch_to.alert
print(alert.text)
assert (name in alert.text)
# Click OK in alert
alert.accept()
#alert.dismiss

time.sleep(3)
driver.close()

