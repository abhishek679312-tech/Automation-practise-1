from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest 

def test_input_type(driver):
    wait=WebDriverWait(driver,10)
    driver.get("https://www.saucedemo.com")
    username=wait.until(EC.visibility_of_element_located((By.ID,"user-name")))
    username.send_keys("test_vendor_user")

    assert username.get_attribute("value")=="test_vendor_user"

    username.send_keys(Keys.CONTROL + "a")
    username.send_keys(Keys.BACKSPACE)

    assert username.get_attribute("value")==""

    