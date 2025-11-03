import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()  # Class ChromeOptions allows to add some config to Chrome
chrome_options.add_argument("headless")  # allows to run Chrome in background, browser is not visible
chrome_options.add_argument("--ignore-certificate-error")

driver = webdriver.Chrome(options=chrome_options)  # adding chrome options to driver

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(2)

# execute_script allows to execute JavaScript to perform some actions in the page like scroll
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")  # take screenshots and save it in screen.png
driver.close()
