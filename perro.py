from animal import Animal


class Perro(Animal):
    # Constructor de la clase Perro
    def __init__(self, nombre, raza, peso, edad):
        super().__init__(nombre, peso, edad)
        # atributos
        self.__raza = raza

# metodos

    def hacer_sonido(self):
        return "Ladrando..."

    def obtener_raza(self):
        return self.__raza
