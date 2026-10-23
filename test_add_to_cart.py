import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.smoke
def test_verify_item_in_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 10)
    # 1. Login
    
    # 2. Add product to cart
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_to_cart_btn.click()
    
    # 3. Verify cart badge update
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    assert cart_badge.text == "1", f"Expected cart badge to show '1', but got '{cart_badge.text}'"

    # 3. Click on the shopping cart icon to navigate to the cart page
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()
    
    # 4. Verify the item title inside the cart
    cart_item_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    
    # 5. Assert that the item in the cart is correct
    assert cart_item_title.text == "Sauce Labs Backpack", f"Expected item 'Sauce Labs Backpack', but got '{cart_item_title.text}'"

    # 4. Proceed to Checkout
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # 5. Fill in Customer Information
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Abhishek")
    driver.find_element(By.ID, "last-name").send_keys("Patil")
    driver.find_element(By.ID, "postal-code").send_keys("560003")

    # 6. Click Continue
    driver.find_element(By.ID, "continue").click()

    # 7. Click Finish
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()

    # 8. Assert Order Completion
    success_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert success_header.text == "Thank you for your order!"