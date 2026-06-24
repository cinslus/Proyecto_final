from page.login_page import loginPage
from utils.logger import logger
import pytest

@pytest.mark.smoke   
def test_login_ok(driver):
    logger.info("Inicializando el driver para test_login_ok")
    login_Page = loginPage(driver)
    logger.info("Ingresando los datos de entrada para la prueba.")
    login_Page.login("standard_user","secret_sauce")
    logger.info("Iniciando sesion.....")
    assert "/inventory.html" in driver.current_url, "No se dirigio al inventario"
    if "/inventory.html" in driver.current_url:
        logger.info("sesion inicializada correctamente.")
    else: logger.info("No se dirigio al inventario")
    
def test_login_invalid_password(driver):
    logger.info("Inicializando el driver para test_login_invalid_password")
    login_Page = loginPage(driver)
    logger.info("Ingresando los datos de entrada para la prueba.")
    login_Page.login("standard_user","123456") 
    
    error = login_Page.get_error_password_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error
    
def test_login_invalid_usuario(driver):
    logger.info("Inicializando el driver para test_login_invalid_usuario.")  
    login_page = loginPage(driver)
    logger.info("Ingresando los datos de entrada para la prueba.")  
    login_page.login("usuario_incorrecto","secret_sauce")
    
    error = login_page.get_error_user_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error