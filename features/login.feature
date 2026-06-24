Feature: Inicio de sesion
    Scenario: Login exitoso
        Given que el usuario este en la pagina de login
        When ingresa el usuario 'standard_user' y clave 'secret_sauce'
        And hace clic en el boton login
        Then deberia ingresar al inventario
        

    Scenario: Login fallido con contraseña incorrecta
        Given que el usuario este en la pagina de login
        When ingresa el usuario 'standard_user' y clave '123456' 
        And hace clic en el boton login
        Then deberia arrojar un mensaje de error 'Epic sadface: Username and password do not match any user in this service'

    Scenario: Login fallido con usuario bloqueado
        Given que el usuario este en la pagina de login
        When ingresa el usuario 'locked_out_user' y clave 'secret_sauce'
        And hace clic en el boton login
        Then deberia arrojar un mensaje de error 'Epic sadface: Sorry, this user has been locked out.'


    Scenario Outline: Login fallido con diferentes usuarios 
        Given que el usuario este en la pagina de login
        When ingresa el usuario '<usuario>' y clave '<password>'
        And hace clic en el boton login
        Then deberia arrojar un mensaje de error '<mensaje>'

        Examples:
        |usuario|password|mensaje|
        |standard_user|password_incorrecto|Epic sadface: Username and password do not match any user in this service|
        |locked_out_user|secret_sauce|Epic sadface: Sorry, this user has been locked out.|
        |standard_user|123456|Epic sadface: Username and password do not match any user in this service|
        |VACIO|VACIO|Epic sadface: Username is required|
        |standard_user|VACIO|Epic sadface: Password is required|
        |VACIO|secret_sauce|Epic sadface: Username is required| 