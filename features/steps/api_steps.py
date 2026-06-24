from behave import given, when,then
import requests

headers = {
    "x-api-key" : "pub_5b7db41d9ad29292d3f7d161476d3b6af25800b4b526d484eb6c7f445f1e27ab"
}
@given("la API de Reqres esta disponible")
def step_impl(context):
    context.base_url = "https://reqres.in/api"
    
@when("realizar un login valido")
def step_impl(context):
    body = {
        "email":"eve.holt@reqres.in",
        "password": "cityslicka"
    }
        
    context.response = requests.post(
        f"{context.base_url}/login",
        headers=headers,
        json=body
    )
    
@then("el status code debe ser {status_code:d}")
def step_impl(context,status_code):
    assert context.response.status_code == status_code
# Scenario 2  
@when("realizar un login sin password")
def step_impl(context):
    body = {
        "email":"eve.holt@reqres.in"
    }
    context.response = requests.post(
        f"{context.base_url}/login",
        headers=headers,
        json=body
    )
    
@then("el mensaje de error debe ser '{mensaje}'")
def step_impl(context,mensaje):
    body = context.response.json()
      
    assert body["error"] == mensaje
    