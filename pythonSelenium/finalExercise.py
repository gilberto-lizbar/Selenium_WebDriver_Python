import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()  # Class ChromeOptions allows to add some config to Chrome
#chrome_options.add_argument("headless")
chrome_options.add_argument("--start-maximized")  # start browser maximized
chrome_options.add_argument("--ignore-certificate-error")

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
action = ActionChains(driver)

wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-nav")))
driver.find_element(By.LINK_TEXT, "Shop").click()

wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='card-body']")))

action.scroll_to_element(driver.find_element(By.CSS_SELECTOR, ".py-5"))
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
#products = driver.find_elements(By.XPATH, "//h4[@class='card-title']/a[@href]")
product_names = []

action.scroll_to_element(driver.find_element(By.CSS_SELECTOR, ".py-5")).perform()

'''for product in products:
    prod_txt = product.find_element(By.XPATH, "//h4[@class='card-title']/a[@href]").text
    product_names.append(prod_txt)
    print(prod_txt)'''
    #product.find_element(By.XPATH, "//button").click()
    #action.scroll_to_element(driver.find_element(By.CSS_SELECTOR, ".py-5"))
    #product_names.append(product.find_element(By.XPATH, "//button").click())
#print(product_names)

for product in products:
    prod_txt = product.find_element(By.XPATH, "div/h4/a").text
    product_names.append(prod_txt)
    product.find_element(By.XPATH, "div/button").click()
    print(prod_txt)

print(product_names)

driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

wait.until(expected_conditions.visibility_of_element_located((
    By.XPATH, "//a[(@class='navbar-brand') and (text()='ProtoCommerce Home')]")))
elements = driver.find_elements(By.CSS_SELECTOR, "h4[class='media-heading']>a")

for i in range(0, len(product_names)):
    prod_txt = elements[i].text
    if prod_txt == product_names[i]:
        print(" Product ", prod_txt, "verified")

driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#country")))
driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Sl")
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Slovenia")))
driver.find_element(By.LINK_TEXT, "Slovenia").click()
#wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Slovenia")))
driver.find_element(By.CSS_SELECTOR, ".checkbox>#checkbox2")
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text

assert "Success! Thank you!" in successText

driver.close()
