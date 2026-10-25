import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.mark.smoke
def test_verify_item_in_cart(logged_in_driver):
    driver = logged_in_driver
    wait = WebDriverWait(driver, 20)
    # 1. Login
    
    # 2. Add product to cart
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))
    add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", add_to_cart_btn)
    add_to_cart_btn.click()
    
    # 3. Verify cart badge update (with retry if React dropped the click during re-render)
    try:
        cart_badge = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
    except Exception:
        add_btn = driver.find_elements(By.ID, "add-to-cart-sauce-labs-backpack")
        if add_btn:
            driver.execute_script("arguments[0].click();", add_btn[0])
        cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    assert cart_badge.text == "1", f"Expected cart badge to show '1', but got '{cart_badge.text}'"

    # 4. Click on the shopping cart icon to navigate to the cart page
    cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_icon.click()
    
    # 5. Verify the item title inside the cart
    cart_item_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name")))
    assert cart_item_title.text == "Sauce Labs Backpack", f"Expected item 'Sauce Labs Backpack', but got '{cart_item_title.text}'"

    # 6. Proceed to Checkout
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()

    # 7. Fill in Customer Information
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Abhishek")
    wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys("Patil")
    wait.until(EC.visibility_of_element_located((By.ID, "postal-code"))).send_keys("560003")

    # 8. Click Continue
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID, "continue")))
    continue_btn.click()

    # 9. Click Finish
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()

    # 10. Assert Order Completion
    success_header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert success_header.text == "Thank you for your order!"