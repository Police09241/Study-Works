class Greeter():
    def __init__(self):
        pass
    
    def hello(self):
        return "Привет!"
    
class FormalGreeter(Greeter):
    def hello(self):
        return super().hello() + "Добрый день" + Greeter.hello(self)

# super().hello() позволяет автоматически подставлять всё то, что есть в родительском класе
# Greeter.hello(self) это буквально прямой вызов

a = FormalGreeter()
b = Greeter()
print(a.hello())