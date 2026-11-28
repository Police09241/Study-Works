class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def income(self):
        return self.salary
    
    def info(self):
        return f"{self.name}: доход {self.income():.0f} руб"
    
class Manager (Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def income(self):
        return super().income() + self.bonus
    
class Developer(Employee):
    def __init__(self, name, salary, level):
        super().__init__(name, salary)
        self.level = level
    
    def income(self):
        k = {1: 1.0, 2: 1.2, 3: 1.5}.get(self.level, 1.0)
        return super().income() * k
    

class Intern(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def income(self):
        return self.hourly_rate * self.hours
    
staff = [Employee("Штатский", 30000), Manager("Админ", 60000, 10000), Developer("Разраб", 50000, 2),
           Intern("Рядовой", 5000, 4)
           ]

for people in staff:
    print(people.info())

print("общий доход:", sum(e.income() for e in staff))