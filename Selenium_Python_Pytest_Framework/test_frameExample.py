import os.path
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Selenium_Python_Pytest_Framework.pageObjects.login import LoginPage


def test_frameExample1(browserInstance):
    driver = browserInstance  # Calling driver from browserInstance fixture
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    # Create an object from LoginPage class to have access to class methods
    loginPage = LoginPage(driver)
    # loginPage.login()
    # shopPage = ShopPage(driver)
    shopPage = loginPage.login()  # Two lines above were changed by this line making login method
    # from login.py file return shopPage objects as: return ShopPage(self.driver), in this way we
    # do not need to create an object of each page

    # Test Steps
    product_names = shopPage.add_product_to_cart()
    checkout_confirmationPage = shopPage.go_to_cart()
    checkout_confirmationPage.verified_Products(product_names)
    checkout_confirmationPage.checkout_Products()
    checkout_confirmationPage.enter_delivery_address("Slovenia")
    checkout_confirmationPage.validate_order()
