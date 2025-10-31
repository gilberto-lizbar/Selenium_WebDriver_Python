import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()


# Fluent wait is an improved explicit wait
wait = WebDriverWait(driver,
                     timeout=20,  # Maximum wait time in seconds
                     poll_frequency=5,  # Check every 1 second
                     ignored_exceptions=[NoSuchElementException,
                                         ElementNotVisibleException,
                                         ElementNotSelectableException])

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".search-keyword")))
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert (count > 0)

for result in results:
    # Chaining of WebElements
    result.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
