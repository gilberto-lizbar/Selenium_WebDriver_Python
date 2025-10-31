import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# Implicit Wait
driver.implicitly_wait(2)  # global time to wait until a line code fails
# It instructs the WebDriver to wait for a certain amount of time before
# throwing a NoSuchElementException if an element is not immediately found on the page.

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert (count > 0)

for result in results:
    # Chaining of WebElements
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr>td:nth-child(5)>p")

prices_sum = 0
for price in prices:
    prices_sum = prices_sum + float(price.text)
print(prices_sum)

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
print(totalAmount)

assert (prices_sum == float(totalAmount))
print("total amount is: $", float(totalAmount))

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Declare a webdriverwait  - Explicit wait
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
code_txt = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(code_txt)
assert (code_txt == "Code applied ..!")
driver.close()






