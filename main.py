import json
from Integrant_A.Car import Car
from Integrant_A.user import user
#Creem 5 instancies per cars i users
cars = [
    Car("ALFA ROMEO", "Giulia", "46.000€", "Diesel"),
    Car("MERCEDES-BENZ", "Clase A", "38.000€", "Diesel"),
    Car("Ferrari", "SF90", "500.000€", "Hibrid-endollable"),
    Car("Aston Martin", "DB11", "148.00O", "Gasolina"),
    Car("Renault", "Twingo petit", "23.000", "Electric")
]

users = [
    user("Joan", "Gago", "contra", "joangago8@gmail.com", "a", "Tots els permisos"),
    user("Aleix", "Alvarez", "contra123", "vsayan777@gmail.com", "b", "Tots els permisos"),
    user("Pablo", "Rosado", "contra1234", "prosado@gmail.com", "a", "Permisos de lectura"),
    user("Edgar", "Romero", "contr", "eromero@gmail.com", "b", "Tots els permisos"),
    user("Carlos", "Sanchez", "contraaaa", "csanchez@gmail.com", "b", "Tots els permisos")
]
#Convertim les dues llistes en llistes de diccionaris
users_list = [u.to_dict() for u in users]

cars_list = [c.to_dict() for c in cars]

#Guardem les llistes en un objecte contenidor
data = {"users":users_list, "cars":cars_list}
#Guardem l'0bjecte en un arxiu format json
with open("json_API/A.json", 'w') as file:
    json.dump(data, file)