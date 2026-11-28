class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        return f"Я {self.name}, мне {self.age} лет"
    def __str__(self):
        return self.__class__.__name__

class Student(Person):
    def __init__(self, name, age, group):
        super().__init__(name, age)
        self.group = group
    def introduce(self):
        return super().introduce() + f"и я состаю в группе {self.group}"
    
peoples = [Person("Девид", 19), Student("Александр", 18, "14-434"), Person("Димдимыч", "много")]

for people in peoples:
    print(people.introduce())
    print(f"{people} это наследник класса Person: {isinstance(peoples[peoples.index(people)], Person)}")