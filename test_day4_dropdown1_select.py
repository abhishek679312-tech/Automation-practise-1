import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def test_dropdown_sort(setup_driver):
    driver = setup_driver
    driver.get("https://www.saucedemo.com")
    
    wait = WebDriverWait(driver, 10)
    
    # 1. Login using explicit waits (bulletproof against slow loading)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    
    # 2. Locate the sort dropdown with explicit wait
    dropdown_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
    
    # 3. Use Select class to choose an option by value ("lohi" = Price: Low to High)
    select = Select(dropdown_element)
    select.select_by_value("lohi")
    
    # 4. Re-locate the dropdown because React re-renders the DOM after sorting
    dropdown_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(dropdown_element)
    
    # 5. Verify that the correct option is selected
    selected_option = select.first_selected_option
    assert "Price (low to high)" in selected_option.text, f"Expected sorting 'Price (low to high)', got '{selected_option.text}'"
