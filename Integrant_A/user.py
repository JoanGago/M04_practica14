"""
Creem una clase amb nom: user. Aquesta clase conté un constructor, 6 atributs, getters i setters, i un mètode amb nom
salutació on es mostren les dades (atributs).
"""
class user:
    def __init__(self, nom, cognom, contrasenya, email, grup, permisos):
        self.nom = nom
        self.cognom = cognom
        self.contrasenya = contrasenya
        self.email = email
        self.grup = grup
        self.permisos = permisos

    def getNom(self):
        return self.nom

    def setNom(self, nom):
        self.nom = nom

    def getCognom(self):
        return self.cognom

    def setCognom(self, cognom):
        self.cognom = cognom

    def getContrasenya(self):
        return self.contrasenya

    def setcContrasenya(self, contrasenya):
        self.contrasenya = contrasenya

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email

    def getGrup(self):
        return self.grup

    def setGrup(self, grup):
        self.grup = grup

    def getPermisos(self):
        return self.permisos

    def setPermisos(self, permisos):
        self.permisos = permisos

    def salutacio(self):
        print(f"Nom i cognom de l'usuari: {self.nom} {self.cognom}, contrasenya: {self.contrasenya}, email: {self.email}, grup: {self.grup}, permisos: {self.permisos}.")

    def to_dict(self):
        return {
            "nom":self.nom,
            "cognom":self.cognom,
            "contrasenya":self.contrasenya,
            "email":self.email,
            "grup":self.grup,
            "permisos":self.permisos
        }