class Cat:
    def __init__(self, nom, raça, edat, pes, color, sexe):
        self.nom = nom
        self.raça = raça
        self.edat = edat
        self.pes = pes
        self.color = color
        self.sexe = sexe


    def get_nom(self):
        return self.nom

    def set_nom(self, nom):
        self.nom = nom

    def get_raça(self):
        return self.raça

    def set_raça(self, raça):
        self.raça = raça

    def get_edat(self):
        return self.edat

    def set_edat(self, edat):
        self.edat = edat

    def get_pes(self):
        return self.pes

    def set_pes(self, pes):
        self.pes = pes

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_sexe(self):
        return self.sexe

    def set_sexe(self, sexe):
        self.sexe = sexe

    def info(self):
        print("Nom: "+ self.nom)
        print("Raça: "+ self.raça)
        print("Edat: "+ self.edat)
        print("Pes: "+ self.pes)
        print("Color: "+ self.color)
        print("Sexe: "+ self.sexe)

    def to_dict(self): #Aquesta funció s’encarrega de convertir l’objecte creat en format json

        return {
            "nom": self.nom,
            "raça": self.raça,
            "edat": self.edat,
            "pes": self.pes,
            "color": self.color,
            "sexe": self.sexe
        }


