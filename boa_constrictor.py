from animalexotico import AnimalExotico


class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_ratones(self, cantidad=1):
        if cantidad > 0:
            self.__ratones_comidos = cantidad
            return True
        else:
            return False

    def obtener_ratones_comidos(self):
        return self.__ratones_comidos


boa1 = BoaConstrictor("Soru", 1.2, 5, "Sudan", 0.2)
boa1.comer_ratones(5)
print(f"Ratones comidos por {boa1.obtener_nombre()}: {boa1.obtener_ratones_comidos()}")
print(f"Sonido de la {boa1.obtener_nombre()}: {boa1.hacer_sonido()}")
