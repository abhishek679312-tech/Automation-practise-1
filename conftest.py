import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_chrome_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--window-size=1920,1080")
    return options

# 1. Base clean browser (for login tests, negative tests, etc.)
@pytest.fixture
def setup_driver():
    options = get_chrome_options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Alias for tests that use 'driver' fixture name
@pytest.fixture
def driver(setup_driver):
    return setup_driver

# 2. Pre-authenticated browser (for cart, checkout, dashboard tests, etc.)
@pytest.fixture
def logged_in_driver():
    options = get_chrome_options()
    options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com")
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    wait.until(EC.visibility_of_element_located((By.ID, "password"))).send_keys("secret_sauce")
    wait.until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
    wait.until(EC.url_contains("/inventory.html"))
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("logged_in_driver") or item.funcargs.get("driver")
        if drv:
            drv.save_screenshot("failure.png")   