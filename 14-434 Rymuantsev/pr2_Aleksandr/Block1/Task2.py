class Person:
    def __init__(self, name, age):
        if not (0 < age <= 120):
            raise ValueError("возраст не тот что надо")
        self.name = name
        self.age = age

    def greet(self):
        return f"Привет, я {self.name}, мне {self.age} лет."

try:
    person1 = Person("Александр", 18)
    person2 = Person("Девил", 19)
    person3 = Person("Инквизитор", 100)
    print(person1.greet())
    print(person2.greet())
    print(person3.greet())
    Vladaka = Person("Владыка тьмы", 1000)
    print(Vladaka.greet())
except ValueError as i:
    print(f"ВЫ НЕ ТАМ ГДЕ НАДО, ВЕДЬ {i}")