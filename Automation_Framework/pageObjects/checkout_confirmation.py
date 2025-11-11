from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Automation_Framework.utils.browserutils import BrowserUtils


class CheckoutConfirmation(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.country_option = None
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_button = (By.XPATH, "//button[contains(text(),'Checkout')]")
        self.country_input = (By.CSS_SELECTOR, "#country")
        #self.country_option = (By.LINK_TEXT, "Slovenia")
        self.checkbox = (By.CSS_SELECTOR, ".checkbox>#checkbox2")
        self.submit_button = (By.CSS_SELECTOR, "[type='submit']")
        self.success_message = (By.CLASS_NAME, "alert-success")

    def verified_Products(self, product_names):
        # Products list text
        elements = self.driver.find_elements(By.CSS_SELECTOR, "h4[class='media-heading']>a")

        for i in range(0, len(product_names)):
            prod_txt = elements[i].text
            if prod_txt == product_names[i]:
                print(" Product ", prod_txt, "verified")

    def checkout_Products(self):
        self.driver.find_element(*self.checkout_button).click()
        # return CheckoutConfirmation(self.driver)

    def enter_delivery_address(self, countryName):
        self.driver.find_element(*self.country_input).send_keys(countryName)
        country_option = (By.XPATH, "//li/a[text()='"+countryName+"']")
        '''self.wait.until(expected_conditions.presence_of_element_located
                        ((By.XPATH, "//li/a[text()='"+countryName+"']")))'''
        self.wait.until(expected_conditions.presence_of_element_located(country_option))
        #self.driver.find_element(*By.LINK_TEXT, countryName).click()
        self.driver.find_element(*country_option).click()
        self.driver.find_element(*self.checkbox)
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text
        assert "Success! Thank you!" in successText
