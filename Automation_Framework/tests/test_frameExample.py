import json
from pathlib import Path

import pytest

from Automation_Framework.pageObjects.login import LoginPage

#test_data_path = '../data/test_frameExample.json'
# Get the absolute path to the data file
current_dir = Path(__file__).resolve().parent  # tests directory
project_root = current_dir.parent  # Automation_Framework directory
test_data_path = project_root / 'data' / 'test_frameExample.json'


with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]  # Storing in a list all content of 'data' key from json


@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)  # Extract test_list and attached to test_list_item
# Send test_list_item as an argument of test method to have access to test_list_item data
def test_frameExample1(browserInstance, test_list_item):
    driver = browserInstance  # Calling driver from browserInstance fixture

    # Create an object from LoginPage class to have access to class methods
    loginPage = LoginPage(driver)
    print(loginPage.getTitle())
    # loginPage.login()
    # shopPage = ShopPage(driver)
    # shopPage = loginPage.login()  # Two lines above were changed by this line making login method
    # from login.py file return shopPage objects as: return ShopPage(self.driver), in this way we
    # do not need to create an object of each page
    shopPage = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])
    # shopPage = loginPage.login()

    # Test Steps
    product_names = shopPage.add_product_to_cart()
    checkout_confirmationPage = shopPage.go_to_cart()
    checkout_confirmationPage.verified_Products(product_names)
    checkout_confirmationPage.checkout_Products()
    # checkout_confirmationPage.enter_delivery_address("Slovenia")
    checkout_confirmationPage.enter_delivery_address(test_list_item["country"])
    checkout_confirmationPage.validate_order()
