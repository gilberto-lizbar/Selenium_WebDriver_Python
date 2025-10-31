import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# Implicit Wait
driver.implicitly_wait(2)  # global time to wait until a line code fails
# It instructs the WebDriver to wait for a certain amount of time before
# throwing a NoSuchElementException if an element is not immediately found on the page.

# Declare a webdriverwait  - Explicit wait
wait = WebDriverWait(driver, 10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert (count > 0)

for result in results:
    # Chaining of WebElements
    result.find_element(By.XPATH, "div/button").click()

# Create an empty list for products
product_list = []
products = driver.find_elements(By.CSS_SELECTOR, "h4[class=product-name]")

for product in products:
    product_list.append(product.text)
    print(product_list)

'''for i in range(0, len(products)):
    product_list.append(products[i].text)   
    print(product_list)'''

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Wait until table is visible
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#productCartTables")))

# Create empty list to store products shown in webpage table
table_list = []
table_products = driver.find_elements(By.CSS_SELECTOR, "tbody>tr>td:nth-child(2)")
# Add the products to list table
for table_product in table_products:
    table_list.append(table_product.text)
    print(table_product.text)
# Verify product_list and table_list has the same size (to ensure store same product quantity)
if len(product_list) == len(table_list):
    # Verify each product of 2 list are same
    for i in range(0, len(product_list)):
        assert (product_list[i] == table_list[i])
        print("product verified ", product_list[i])
else:
    print(len(product_list), "and", len(table_list))
    raise Exception("El total de productos de la busqueda y la tabla no es el mismo")

# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr>td:nth-child(5)>p")

prices_sum = 0
for price in prices:
    prices_sum = prices_sum + float(price.text)
print(prices_sum)

totalAmount = driver.find_element(By.CSS_SELECTOR, ".totAmt").text
print(totalAmount)

assert (prices_sum == float(totalAmount))
print("total amount is: $", float(totalAmount))

# Verify Discount before applied code
discount_per_txt = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
assert (discount_per_txt == "0%")
print("Discount percentage ", discount_per_txt)

no_discount_amount_txt = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert (float(no_discount_amount_txt) == prices_sum)
print("amount with no discount $", float(no_discount_amount_txt))

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
code_txt = driver.find_element(By.CLASS_NAME, "promoInfo").text
print(code_txt)
assert (code_txt == "Code applied ..!")

# Verify Discount After applied code
apply_discount_txt = driver.find_element(By.CSS_SELECTOR, ".discountPerc").text
assert (apply_discount_txt != "0%")
print("Discount percentage ", apply_discount_txt)
# Verify Discount amount after applied code
apply_discount_amount_txt = driver.find_element(By.CSS_SELECTOR, ".discountAmt").text
assert (float(apply_discount_amount_txt) < float(prices_sum))
print(f"amount with no discount $ {float(no_discount_amount_txt)} \n"
      f"amount with no discount $ {float(apply_discount_amount_txt)} \n"
      f"discounted amount: $ {float(no_discount_amount_txt) - float(apply_discount_amount_txt)}")

driver.close()
