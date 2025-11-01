from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Click Here").click()


# List of windows opened in the browser
windowsOpened = driver.window_handles
for window in windowsOpened:
    print(window.title())

# When another window is open transfer the focus to that window
driver.switch_to.window(windowsOpened[1])  # Child Window windowsOpened[1]
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()
driver.switch_to.window(windowsOpened[0])  # Main Window
assert (driver.find_element(By.TAG_NAME, "h3").text == "Opening a new window")
driver.close()




