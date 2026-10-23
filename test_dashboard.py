import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def setup_driver():
    driver=webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()

def test_saucedemo_login(setup_driver):
    driver=setup_driver
    driver.get("https://www.saucedemo.com")

    try:
        wait=WebDriverWait(driver,10)
        username=wait.until(EC.visibility_of_element_located((By.ID,"user-name")))
        username.send_keys("standard_user")
        password=wait.until(EC.visibility_of_element_located((By.ID,"password")))
        password.send_keys("secret_sauce")
        login_btn=wait.until(EC.element_to_be_clickable((By.ID,"login-button")))
        login_btn.click()

        wait.until(EC.url_contains("/inventory.html"))
        assert "inventory.html" in driver.current_url
    finally:
        pass
