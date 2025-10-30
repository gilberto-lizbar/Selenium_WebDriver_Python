import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/client/")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# below XPATH can be written as CSS selector as: form>div:nth-child(1)>input
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")

driver.find_element(By.CSS_SELECTOR, "form>div:nth-child(2)>input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[text()='Save New Password']").send_keys("Hello@1234")
time.sleep(2)

driver.close()




