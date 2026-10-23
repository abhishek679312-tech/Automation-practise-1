from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        
        # Locators
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.XPATH, "//h3[@data-test='error']")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        el = self.wait.until(EC.visibility_of_element_located(self.username_field))
        el.clear()
        el.send_keys(username)

    def enter_password(self, password):
        el = self.wait.until(EC.visibility_of_element_located(self.password_field))
        el.clear()
        el.send_keys(password)

    def click_login(self):
        el = self.wait.until(EC.element_to_be_clickable(self.login_button))
        el.click()

    def get_error_text(self):
        el = self.wait.until(EC.visibility_of_element_located(self.error_message))
        return el.text