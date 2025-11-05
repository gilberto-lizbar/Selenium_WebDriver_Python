import time

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path = "/Users/gilberto.barraza/Desktop/Repo_Cursos/Documents_repo/download.xlsx"
fruit_name = "Apple"
newValue = "345"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # start browser maximized
# chrome_options.add_argument("headless")r
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID, "downloadButton").click()

# edit the Excel with updated value
file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
file_input.send_keys(file_path)

wait = WebDriverWait(driver, 10)
toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))

# The * operator in driver.find_element(*toast_locator) is Python's unpacking operator.
# Why it's needed:
# toast_locator is a tuple containing two elements:
# toast_locator = (By.CSS_SELECTOR, ".Toastify__toast-body div:nth-child(2)")
print(driver.find_element(*toast_locator).text)
# Without the * (won't work):
# print(driver.find_element(*toast_locator).text)
# This passes ONE argument (a tuple), but find_element expects TWO arguments

priceColumn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
actual_price = driver.find_element(By.XPATH,
                                   "//div[text()='" + fruit_name + "']/parent::div/parent::div/div[@id='cell-" +
                                   priceColumn + "-undefined']").text
print(actual_price)
assert actual_price == newValue

time.sleep(5)
driver.close()
