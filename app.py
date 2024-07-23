from flask import Flask, jsonify, render_template

app = Flask(__name__)


class Animal:
    def __init__(self, nombre, peso, edad):
        self.__nombre = nombre
        self.__peso = peso
        self.__edad = edad

    def obtener_nombre(self):
        return self.__nombre


class AnimalExotico(Animal):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad)
        self.__pais_origen = pais_origen
        self.__impuestos = impuestos


class Huron(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)

    def hacer_sonido(self):
        return "¡Eek Eek!"


class BoaConstrictor(AnimalExotico):
    def __init__(self, nombre, peso, edad, pais_origen, impuestos):
        super().__init__(nombre, peso, edad, pais_origen, impuestos)
        self.__ratones_comidos = 0

    def hacer_sonido(self):
        return "¡Tsss!"

    def comer_ratones(self, cantidad=1):
        if cantidad >= 20:
            raise ValueError("Demasiados Ratones!")
        if cantidad > 0:
            self.__ratones_comidos = cantidad
            return True
        else:
            return False

    def obtener_ratones_comidos(self):
        return self.__ratones_comidos


class Gato(Animal):
    def __init__(self, nombre, color, peso, edad):
        super().__init__(nombre, peso, edad)
        self.__color = color

    def hacer_sonido(self):
        return "Maullando..."

    def obtener_color(self):
        return self.__color


class Perro(Animal):
    def __init__(self, nombre, raza, peso, edad):
        super().__init__(nombre, peso, edad)
        self.__raza = raza

    def hacer_sonido(self):
        return "Ladrando..."

    def obtener_raza(self):
        return self.__raza


@app.route('/api/sonido/<animal>', methods=['GET'])
def obtener_sonido(animal):
    if animal.lower() == 'perro':
        animal_obj = Perro("Rex", "Labrador", 30, 5)
    elif animal.lower() == 'gato':
        animal_obj = Gato("Miau", "Negro", 5, 3)
    elif animal.lower() == 'huron':
        animal_obj = Huron("Furry", 1.2, 2, "EEUU", 0.08)
    elif animal.lower() == 'boa':
        animal_obj = BoaConstrictor("Soru", 1.2, 5, "Sudan", 0.2)
    else:
        return jsonify({"error": "Animal no encontrado"}), 404

    return jsonify({"nombre": animal_obj.obtener_nombre(), "sonido": animal_obj.hacer_sonido()})


@app.route('/')
def index():
    return render_template('endpoints.html')


if __name__ == '__main__':
    app.run(debug=True)
