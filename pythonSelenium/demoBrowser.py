import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome driver service

# Call Driver using class Service only if webDriver.Chrome() does not work
# Download chromedriver for your Google Chrome browser add the path to Service class
# Then save in driver variable the service_obj for webdriver.chrome
'''service_obj = Service("/Users/gilberto.barraza/Desktop/Repo_Cursos/WebDrivers/chromedriver")
driver = webdriver.chrome(service=service_obj)'''

#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver = webdriver.Safari()
driver.get("https://rahulshettyacademy.com")
# Maximize browser window
driver.maximize_window()
# Get webpage title
print(driver.title)
# Get webpage url
print(driver.current_url)
# Close browser
driver.close()
#time.sleep(2)
