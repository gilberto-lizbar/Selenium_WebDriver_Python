import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item']>a")
print(len(countries))

for country in countries:
    country_txt = country.text
    if country_txt == "India":
        country.click()
        break

# This for loop is valid too
'''for i in range(0, len(countries)):
    country_txt = countries[i].text
    if country_txt == "India":
        countries[i].click()
        break'''

# When update a value dynamically through script we use 'value' attribute to extract the text
val = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert (val == "India")
time.sleep(5)


