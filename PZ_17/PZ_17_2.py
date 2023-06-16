# Вариант 29.
# создайте базовый класс "Животное" со свойствами "вид", "кол-во лап", "цвет шерсти"
# от этого класса унаследуйте класс "собака" и добавьте в него свойства "кличка" и "порода"

class Animal:
    def __init__(self, kind, num_paws, fur_color):
        self.kind = kind
        self.num_paws = num_paws
        self. fur_color = fur_color


class Dog(Animal):
    def __init__(self, kind, num_paws, fur_color, name, breed):
        super().__init__(kind, num_paws, fur_color)
        self.name = name
        self.breed = breed


animal = Animal("Мустанг", 4, "Коричневый")
print(animal.kind)
print(animal.num_paws)
print(animal.fur_color)

dog = Dog("Мустанг", 4, "Коричневый", "Форд", "Лабрадор")
print(dog.kind)
print(dog.num_paws)
print(dog.fur_color)
print(dog.name)
print(dog.breed)
