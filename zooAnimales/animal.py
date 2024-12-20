class Animal():
    totalAnimales=0
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre=nombre
        self._edad=edad
        self._habitat=habitat
        self._genero=genero
        self._zona=zona
        Animal.totalAnimales+=1
    def movimiento():
        return "desplazarse"
    @classmethod
    def totalPorTipo(self):
        from .anfibio import Anfibio
        from .ave import Ave
        from .mamifero import Mamifero
        from .pez import Pez
        from .reptil import Reptil

        cantidad_mamiferos = len(Mamifero._listado)
        cantidad_aves = len(Ave._listado)
        cantidad_reptiles = len(Reptil._listado)
        cantidad_anfibios = len(Anfibio._listado)
        cantidad_peces = len(Pez._listado)
        cantidad_mamiferos = len(Mamifero._listado)
        cantidad_aves = len(Ave._listado)
        cantidad_reptiles = len(Reptil._listado)
        cantidad_anfibios = len(Anfibio._listado)
        cantidad_peces = len(Pez._listado)
        return f"Mamiferos : {cantidad_mamiferos}\nAves : {cantidad_aves}\nReptiles : {cantidad_reptiles}\nPeces : {cantidad_peces}\nAnfibios : {cantidad_anfibios}"
    def toString(self):
        if self.genero==None and self.zona==None:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat}, y mi género es {self._genero}."
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self._edad}, habito en {self._habitat}, y mi género es {self._genero}.\nLa zona en la que me ubico es {self._zona._nombre}, en el {self._zona._zoo._nombre}."
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre
    @classmethod
    def getTotalAnimales(self):
        return Animal.totalAnimales
    @classmethod
    def setTotalAnimales(self,total):
        Animal.totalAnimales=total
    def getEdad(self):
        return self._edad
    def setEdad(self,edad):
        self._edad=edad
    def getHabitat(self):
        return self._habitat
    def setHabitat(self,habitat):
        self._habitat=habitat
    def getGenero(self):
        return self._genero
    def setGenero(self,genero):
        self._genero=genero
    def getZona(self):
        return self._zona
    def setZona(self,zona):
        self._zona=zona