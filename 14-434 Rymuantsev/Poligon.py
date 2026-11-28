class Animal:
    """Базовый класс животного."""
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Какой-то звук"
    def describe(self):
        return f"{self.name}: {self.speak()}" # вызов своего метода
    def __str__(self):
        return self.__class__.__name__

class Dog(Animal):
    """Производный класс: добавляет породу и переопределяет speak()."""
    def __init__(self, name, breed):
        super().__init__(name) # инициализация базовой части
        self.breed = breed # собственный атрибут
    def speak(self): # переопределение метода
        return "Гав!"
    

class Cat(Animal):
    """Свой __init__ не нужен: полностью наследует базовый."""
    def speak(self):
        return "Мяу!"
    


zoo = [Dog("Рекс", "овчарка"), Cat("Мурка")]

for animal in zoo:
    print(zoo.index(animal))

    print(animal.describe()) # Рекс: Гав! / Мурка: Мяу!
    print(isinstance(zoo[zoo.index(animal)], Animal)) # True — Рекс является животным
    print(issubclass(Cat, Animal)) # True — класс-наследник

