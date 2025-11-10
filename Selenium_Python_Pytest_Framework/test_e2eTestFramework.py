import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Python_Pytest_Framework.pageObjects.login import LoginPage


# from selenium import webdriver

def test_e2e(browserInstance):
    driver = browserInstance  # Calling driver from browserInstance fixture
    # driver.get("https://rahulshettyacademy.com/angularpractice")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    # Create an object from LoginPage class to have access to class methods
    loginPage = LoginPage(driver)
    # loginPage.login()
    # shopPage = ShopPage(driver)
    shopPage = loginPage.login()  # Two lines above were changed by this line making login method
    # in login.py file return shopPage object as: return ShopPage(self.driver)

    wait = WebDriverWait(driver, 10)
    action = ActionChains(driver)
    '''
    # **********Steps for login page*****************
    driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
    driver.find_element(By.NAME, "password").send_keys("learning")
    driver.find_element(By.ID, "signInBtn").click()
    # ***********************************************'''

    # wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".navbar-nav")))
    # driver.find_element(By.LINK_TEXT, "Shop").click()

    '''wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='card-body']")))

    products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    product_names = []

    # action.scroll_to_element(driver.find_element(By.CSS_SELECTOR, ".py-5")).perform()

    for product in products:
        prod_txt = product.find_element(By.XPATH, "div/h4/a").text
        product_names.append(prod_txt)
        product.find_element(By.XPATH, "div/button").click()
        print(prod_txt)'''

    product_names = shopPage.add_product_to_cart()
    print(product_names)

    # driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    # shopPage.go_to_cart()
    checkout_confirmationPage = shopPage.go_to_cart()

    wait.until(expected_conditions.visibility_of_element_located((
        By.XPATH, "//a[(@class='navbar-brand') and (text()='ProtoCommerce Home')]")))
    '''elements = driver.find_elements(By.CSS_SELECTOR, "h4[class='media-heading']>a")

    for i in range(0, len(product_names)):
        prod_txt = elements[i].text
        if prod_txt == product_names[i]:
            print(" Product ", prod_txt, "verified")'''
    checkout_confirmationPage.verified_Products(product_names)

    # driver.find_element(By.XPATH, "//button[contains(text(),'Checkout')]").click()
    checkout_confirmationPage.checkout_Products()

    '''driver.find_element(By.CSS_SELECTOR, "#country").send_keys("Sl")
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Slovenia")))
    driver.find_element(By.LINK_TEXT, "Slovenia").click()
    driver.find_element(By.CSS_SELECTOR, ".checkbox>#checkbox2")
    driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
    successText = driver.find_element(By.CLASS_NAME, "alert-success").text

    assert "Success! Thank you!" in successText'''

    checkout_confirmationPage.enter_delivery_address("Slovenia")
    checkout_confirmationPage.validate_order()
