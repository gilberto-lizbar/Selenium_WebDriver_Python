from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://the-internet.herokuapp.com/iframe")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@role='alert']")))
driver.find_element(By.XPATH, "//div[@role='alert']//button").click()
driver.switch_to.frame("mce_0_ifr")  # use id or name to detect frame
# Lines below were commented due the webeditor is disabled
# driver.find_element(By.ID, "tinymce").clear()
# driver.find_element(By.ID, "tinymce").send_keys("I am able to automate frames")
print(driver.find_element(By.ID, "tinymce").text)
# Switch back to the content outside frames
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, "h3").text)
driver.close()

