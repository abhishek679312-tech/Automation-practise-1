import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_chrome_options():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    return options

# 1. Base clean browser (for login tests, negative tests, etc.)
@pytest.fixture
def setup_driver():
    driver = webdriver.Chrome(options=get_chrome_options())
    yield driver
    driver.quit()

# 2. Pre-authenticated browser (for cart, checkout, dashboard tests, etc.)
@pytest.fixture
def logged_in_driver():
    driver = webdriver.Chrome(options=get_chrome_options())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()