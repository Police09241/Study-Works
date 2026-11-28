class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return f"{self.name} стоит {self.price}"
try:
    class DiscountedProduct(Product):
        def __init__(self, name, price, discount):
            self.discount = discount

    a = DiscountedProduct("Банан", 30, 2)
    print(a)

except Exception as e:
    print(f"Произошла ошибка: {e}")
# Произошла ошибка: 'DiscountedProduct' object has no attribute 'name' --
## данная ошибка произошла, т. к. из за отсутсвия super().__init__(name, price), name просто не инициализировался

class DiscountedProduct(Product):
   def __init__(self, name, price, discount):
       super().__init__(name, price)
       self.discount = discount

a = DiscountedProduct("Банан", 30, 2)
print(a)