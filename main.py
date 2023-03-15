import json
from Integrant_A.Car import Car
from Integrant_A.user import user
from Integrant_B.Cat import Cat
from Integrant_B.book import book
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


cats = [
    Cat("Blacky","Bombay","11","4","Negre","Masculi"),
    Cat("Coco","Egipci","2","3","Blanc","Masculi"),
    Cat("Luna","Balines", "5", "5","Blanc amb taques negres","Femeni"),
    Cat("Roma","Birmano","16","6","Taronja","Femeni"),
    Cat("Wilson","Peterbald","7","4","Negre","Masculi")
]


books = [
    book(" Harry Potter", " Pablo Rosado", " Norma Editorial", " 345", " Dura", " Català"),
    book(" Ets galàctica, Carlota", " Edgar Romero", " Catalonia Editorial", " 268", " Tova", " Català"),
    book(" Don Quijote", " Carlos Sanchez", " Algar Editorial", " 324", " Tova", " Castellà"),
    book(" El principito", " Joan Gago", " Sudamericana Editorial", " 235", " Tova", " Castellà"),
    book(" Hobbit", " Aleix Avarez", " Tolkien Editorial", " 452", " Dura", " Català")
]
#Convertim les dues llistes en llistes de diccionaris
users_list = [u.to_dict() for u in users]

cars_list = [c.to_dict() for c in cars]

cats_list = [g.to_dict() for g in cats]

books_list = [b.to_dict() for b in books]

#Guardem les llistes en un objecte contenidor
data = {"users":users_list, "cars":cars_list}
dat = {"cats":cats_list, "books":books_list}

#Guardem l'0bjecte en un arxiu format json
with open("json_API/A.json", 'w') as file:
    json.dump(data, file)

with open("json_API/B.json", 'w') as file:
    json.dump(dat, file)
