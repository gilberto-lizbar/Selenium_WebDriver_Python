from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
openedWindows = driver.window_handles
driver.switch_to.window(openedWindows[1])
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".im-para.red")))
print(driver.find_element(By.CSS_SELECTOR, ".im-para.red").text)
text_spl = driver.find_element(By.CSS_SELECTOR, ".im-para.red").text
spl_list = text_spl.split(" ")
email = ""
for split_item in spl_list:
    if "@rahulshettyacademy.com" in split_item:
        email = split_item
driver.close()
driver.switch_to.window(openedWindows[0])
driver.find_element(By.NAME, "username").send_keys(email)
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("Test$1234")
driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "alert")))
alert_txt = driver.find_element(By.CLASS_NAME, "alert").text
print(alert_txt)
driver.close()



