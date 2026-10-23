import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1. Base clean browser (for login tests, negative tests, etc.)
@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

# 2. Pre-authenticated browser (for cart, checkout, dashboard tests)
@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    yield driver
    driver.quit()
