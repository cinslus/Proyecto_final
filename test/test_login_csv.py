from page.login_page import loginPage
from utils.data_reader import read_users_csv
import pytest


@pytest.mark.parametrize("user",read_users_csv())
def test_login(driver,user):
    login_page = loginPage(driver)

    login_page.login(user["username"],user["password"])
    if user["valid"] == "true":
        assert "/inventory.html" in driver.current_url, "No se redirigió al inventario"
    else:
        error = login_page.get_error_password_message() 
        assert "Epic sadface:" in error