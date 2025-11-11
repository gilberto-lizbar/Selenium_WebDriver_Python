from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Selenium_Python_Pytest_Framework.pageObjects.checkout_confirmation import CheckoutConfirmation
from Selenium_Python_Pytest_Framework.utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.shop_link = (By.LINK_TEXT, "Shop")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, ".btn-primary")
        self.checkout_bar = (By.CSS_SELECTOR, ".navbar-nav")

    def add_product_to_cart(self):
        # self.wait.until(expected_conditions.visibility_of_element_located(self.shop_link))
        self.wait.until(expected_conditions.visibility_of_element_located
                        (self.checkout_bar))
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements()
        product_names = []

        for product in products:
            prod_txt = product.find_element(By.XPATH, "div/h4/a").text
            product_names.append(prod_txt)
            product.find_element(By.XPATH, "div/button").click()
            print(prod_txt)
        print(product_names)
        return product_names

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_button).click()
        return CheckoutConfirmation(self.driver)
