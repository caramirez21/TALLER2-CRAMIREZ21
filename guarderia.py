from perro import Perro
from ianimal import iAnimal
from animal import Animal
from animal_granja import Animal_Granja


perro_1 = Perro("Zeus", "Rottweiler", 45.8, 3)
perro_2 = Perro("Nala", "Golden R.", 8.5, 0)
perro_3 = Perro("Atila", "Alabai", 58.9, 5)

print("Es Perro")
print(isinstance(perro_1, Perro))
print("Es Animal")
print(isinstance(perro_1, Animal))
print("Es iAnimal")
print(isinstance(perro_1, iAnimal))
print("Es Animal_Granja")
print(isinstance(perro_1, Animal_Granja))
