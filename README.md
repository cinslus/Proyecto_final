# Proyecto de Automatizacion QA - Sluszkiewicz Cintia

## Descripcion

Este repositorio contiene un Framework de Automatización de Pruebas E2E (End-to-End) diseñado para validar la funcionalidad de una aplicación web (https://www.saucedemo.com/). 
## Tecnologias usadas
- Lenguaje : Python
- Automatizacion de Navegador : Selenium WebDriver
- Framework de Pruebas: Pytest
- Reportes: Pytest HTML
- Control de versiones: Git

## Instalacion

`git clone https:https://github.com/cinslus/TrabajoFinal`

## Instalacion de dependencias

`pip install -r requirements.txt`

## Funcionamiento de las pruebas

- Test login: Verifica que el proceso de autenticacion redirija al usuario a la pagina correcta. Validacion de URL

- Test cart: -Validación de agregado de productos desde el home.
             -Verificación de persistencia de productos en el carrito.
             -Cálculo correcto de totales y cantidades.

- Test inventory: - test_inventory_title (Verificación de Integridad)
Acción: Obtiene el título de la pestaña del navegador.
Objetivo: Validar que el usuario se encuentra efectivamente en la aplicación correcta ("Swag Labs").(smoke test) .
                  - test_productos_visibles (Verificación de Contenido) Asegura que el catálogo no esté vacío. 
                  - test_ui_elements (Verificación de Componentes Críticos)
 Se encarga de verificar que los elementos de navegación y control estén visibles para el usuario.
