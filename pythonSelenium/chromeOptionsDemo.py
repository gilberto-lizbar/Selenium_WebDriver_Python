from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # start browser maximized
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)

# driver = webdriver.Chrome(executable_path=" path of chrome driver here", options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
driver.get_screenshot_as_file("screen.png")
driver.close()

