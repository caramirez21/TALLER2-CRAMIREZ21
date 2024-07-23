from animal import Animal


class Gato(Animal):
    # Constructor de la clase Perro
    def __init__(self, nombre, color, peso, edad):
        super().__init__(nombre, peso, edad)
        # atributos
        self.__color = color

    # metodos

    def hacer_sonido(self):
        return "Maullando..."

    def obtener_color(self):
        return self.__color
