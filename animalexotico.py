from animal import Animal


class AnimalExotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos

    def calcular_flete(self):
        return self.__impuestos * self.obtener_peso()

    def obtener_pais_origen(self):
        return self.__pais_origen

    def obtener_impuestos(self):
        return self.__impuestos

# Uso Clase
aexotico1 = AnimalExotico("Chaux", 120, 4, "Australia", 1000)
# print(f"Flete para {aexotico1.obtener_nombre()}: {aexotico1.calcular_flete()}")
