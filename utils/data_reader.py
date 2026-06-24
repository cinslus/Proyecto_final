import csv
import json

def read_users_csv():
    with open("data/users.csv",newline="") as file: # abro el proyecto, lo define
        reader = csv.DictReader(file) #lo convierto a diccionario
        return list(reader)#lo convierte en lista
    
def read_products_json():   #
    with open("data/product.json") as file:
        return json.load(file)
    