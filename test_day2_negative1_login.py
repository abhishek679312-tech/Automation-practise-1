import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_error", [
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
    ("wrong_user", "wrong_pass", "Epic sadface: Username and password do not match any user in this service"),
    ("", "secret_sauce", "Epic sadface: Username is required")
])
def test_negative_login_pom(setup_driver, username, password, expected_error):
    # Notice we put `setup_driver` here. Pytest automatically opens Chrome for you!
    login_page = LoginPage(setup_driver)
    
    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    
    error_text = login_page.get_error_text()
    assert expected_error in error_text