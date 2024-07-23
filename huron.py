from animalexotico import AnimalExotico


class Huron(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
    def hacer_sonido(self):
        return "¡Eek Eek!"


huron = Huron("Hurón", 1.2, 2, "EEUU", 0.08)
print(f"Sonido del {huron.obtener_nombre()}: {huron.hacer_sonido()}")
