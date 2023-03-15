"""
Creem una clase amb nom: Car. Aquesta clase conté un constructor, 4 atributs, getters i setters, un mètode amb nom
salutació on es mostren les dades (atributs) de car i un metode to_dict(self).
"""
class Car:
    def __init__(self, marca, model, preu, combustible):
        self.marca = marca
        self.model = model
        self.preu = preu
        self.combustible = combustible

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getModel(self):
        return self.model

    def setModel(self, model):
        self.model = model

    def getPreu(self):
        return self.preu

    def setPreu(self, preu):
        self.preu = preu

    def getCombustible(self):
        return self.combustible

    def setCombustible(self, combustible):
        self.combustible = combustible

    def salutacio(self):
        print(
            f"La marca del cotxe és: {self.marca}.\n"
            f"El model és: {self.model}.\n"
            f"El preu és:{self.preu}.\n"
            f"El combustible que utilitza és: {self.combustible}.\n"
        )

    def to_dict(self):
        return {
            "marca":self.marca,
            "model":self.model,
            "preu":self.preu,
            "combustible":self.combustible
        }

