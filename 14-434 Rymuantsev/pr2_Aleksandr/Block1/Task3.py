class Car:
    def __init__(self, brend, model, age):
        self.brend = brend
        self.model = model
        self.age = age
    def info(self):
        return f"Бренд {self.brend}; Модель {self.model}; Возраст {self.age}"
    def __str__(self):
        pass


Honda = Car("Honda", 3, 1987)
Mark = Car("Toyota", 6, 1989)