class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Какой то звук"
    def info(self):
        return f"{self.name}: {self.speak()}"
    def __str__(self):
        return self.__class__.__name__



class Dog(Animal):
    def speak(self):
        return "Гав"
    
class Cat(Animal):
    def speak(self):
        return "Мяу"
    
class Cow(Animal):
    def speak(self):
        return "Мууууу"
    

animals = [Dog("Собака"), Cat("Кот"), Cow("Корова")]
for animal in animals:
    print(animal.info())

    print(f"{animal} это животноое: {isinstance(animals[0], Animal)}") # True — Рекс является животным
    print(f"{animal} Наследник {issubclass(Cat, Animal)}") # True — класс-наследник
