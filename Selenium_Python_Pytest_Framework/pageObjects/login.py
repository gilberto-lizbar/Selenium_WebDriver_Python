from selenium.webdriver.common.by import By

from Selenium_Python_Pytest_Framework.pageObjects.shop import ShopPage


class LoginPage:

    # Declare locators in constructor and attach to 'self' to access anywhere in the class,
    # self allows methods to access and modify the attributes (variables) that belong to a +
    # specific instance of the class.
    def __init__(self, driver):  # Add driver as an argument of constructor to force whoever
        # call page class to activate the driver
        self.driver = driver
        self.username_input = (By.ID, "username")  # packaging tuple
        self.password = (By.NAME, "password")
        self.sign_button = (By.ID, "signInBtn")

    def login(self):
        # self.username_input is recognized as 1 argument in driver.find_element(self.username_input)
        # to split original tupple (By.ID, "username") into 2 arguments you need to add *
        # before the variable like this: *self.username_input (packaging tuple)

        # self.driver.find_element(self.username_input).send_keys("rahulshettyacademy")  # do not work
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")  # works
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.sign_button).click()
        return ShopPage(self.driver)
