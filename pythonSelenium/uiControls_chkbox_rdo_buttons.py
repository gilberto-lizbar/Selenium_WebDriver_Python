import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
cb_example = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

# print values from checkboxes way 1
for checkbox in cb_example:
    cb_txt = checkbox.get_attribute("value")
    print(cb_txt)
# print values from checkboxes way 2
for i in range(0, len(cb_example)):
    cb_txt = cb_example[i].get_attribute("value")
    print(cb_txt)
    if cb_txt == "option2":
        cb_example[i].click()
        assert (cb_example[i].is_selected())
        break

rd_example = driver.find_elements(By.XPATH,  "//input[@name='radioButton']")

for radio_button in rd_example:
    rd_txt = radio_button.get_attribute("value")
    radio_button.click()
    print(rd_txt)

assert (rd_example[2].is_selected())
assert (driver.find_element(By.ID, "displayed-text").is_displayed())
driver.find_element(By.CSS_SELECTOR, "#hide-textbox").click()
assert not (driver.find_element(By.ID, "displayed-text").is_displayed())
time.sleep(3)
driver.close()
