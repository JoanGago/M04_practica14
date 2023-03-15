class book:
    def __init__(self, titol, autor, editorial, pagines, portada, idioma):   #Crea un constructor
        self.titol = titol
        self.autor = autor
        self.editorial = editorial
        self.pagines = pagines
        self.portada = portada
        self.idioma = idioma

    def getTitol(self): #Crea un getter
        return self.titol

    def setTitol(self, titol): #Crea un setter
        self.titol = titol

    def getAutor(self):
        return self.autor

    def setAutor(self, autor):
        self.autor = autor

    def getEditorial(self):
        return self.editorial

    def setEditorial(self, editorial):
        self.editorial = editorial

    def getPagines(self):
        return self.pagines

    def setPagines(self, pagines):
        self.pagines = pagines

    def getPortada(self):
        return self.portada

    def setPortada(self, portada):
        self.portada = portada

    def getIdioma(self):
        return self.idioma

    def setIdioma(self, idioma):
        self.idioma = idioma

    def informacio(self):  #Crea una instancia
        print("Títol:" + self.titol)
        print("Autor:" + self.autor)
        print("Editorial:" + self.editorial)
        print("Pàgines:" + self.pagines)
        print("Portada:" + self.portada)
        print("Idioma:" + self.idioma)

    def to_dict(self):
        return {
            "titol": self.titol,
            "autor": self.autor,
            "editorial": self.editorial,
            "pagines": self.pagines,
            "portada": self.portada,
            "idioma": self.idioma
            }

