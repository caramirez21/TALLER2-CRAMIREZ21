from ianimal import iAnimal


class Animal_Granja (iAnimal):
    def __init__(self, nombre, peso, edad):
        self.__kilos_comidos = 0

    def comer(self, kilos):
        self.__kilos_comidos = (kilos*0.8)

    def obtener_kilos_comidos(self):
        return self.__kilos_comidos
