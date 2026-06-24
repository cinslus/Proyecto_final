from page.login_page import loginPage
from behave import given, when, then

@given("que el usuario este en la pagina de login")
def step_uuario_en_login(context):
    context.login_page = loginPage(context.driver)
    context.login_page.open()
    
@when("ingresa el usuario '{usuario}' y clave '{password}'")
def step_ingresar_credenciales(context,usuario,password):
    if usuario == "VACIO":
        usuario= ""
    if password == "VACIO":
        password = ""
    
    context.login_page.ingresar_usuario(usuario)
    context.login_page.ingresar_password(password)
    
@when("hace clic en el boton login")
def step_click_login(context):
    context.login_page.click_login()

@then("deberia ingresar al inventario")
def step_validar_login_exitoso(context):
    assert "/inventory.html" in context.driver.current_url, "No se dirigio al inventario"
    
@then("deberia arrojar un mensaje de error '{mensaje}'")
def step_validar_mensaje_error_contraseña_invalida(context,mensaje):
    error = context.login_page.get_error_login_message()
    assert mensaje in error, f"se esperaba '{mensaje}', pero se obtuvo '{error}'"
    

    
