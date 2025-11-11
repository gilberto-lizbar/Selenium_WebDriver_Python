class BrowserUtils:

    def __init__(self, driver):
        self.driver = driver

    # Here add all commons reussable functions
    def getTitle(self):
        return self.driver.title
