from selenium import webdriver
from selenium.webdriver.common.by import By

browserSortedVeggies = []

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(5)

# click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# collect all veggie names -> BrowserSortedveggieList
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for veggie in veggieWebElements:
    browserSortedVeggies.append(veggie.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this BrowserSortedveggieList => newSortedList
browserSortedVeggies.sort()  # Sort the actual browserSortedVeggies
# new_list = sorted(browserSortedVeggies)  # Creates a new sorted list

assert (browserSortedVeggies == originalBrowserSortedList)
# BrowserSortedveggieList == new SortedList

driver.close()
