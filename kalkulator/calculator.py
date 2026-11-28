def addition (a, b):
    return a + b

def subtraction (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    if b == 0:
        print("На 0 делить нельзя")
        return a
    return a / b

def exponentiation (a, i):
    return a**i

def extracting (a):
    return a**0.5

def factorial (n):
    if n < 0:
        print("Число должно быть положительным")
        return n
    if n.is_integer():
        n = int(n)
        print(n)
    else:
        print("Число должно быть целым")
        return n
    result = 1
    for i in range(2, n + 1):
        result *= i
    result = float(result)
    return result

if __name__ == "__main__":
    print("Добро пожаловать в самодельный калькулятор \n" \
    "--------------------------------------------- \n" \
    "---Навигация---\n" \
    "Сложение: '+'\n" \
    "Вычитание: '-'\n" \
    "Умножение: '*'\n" \
    "Деление: '/' \n" \
    "Возведение в степент: '**'\n" \
    "Извлечение квадратного корня: '/**'\n" \
    "Факториал: 'n!' \n" )
    "Обнуление калькулятор: Enter"
    zag = "Введите число: "

    while True:
        a = float(input("Введите начально число: "))
        while True:
            dev = input("Что вы хотите с ним сделать: ")
            if dev == "+":
                a = addition(a, float(input(zag)))
            elif dev == "-": 
                a = subtraction(a, float(input(zag)))
            elif dev == "*":
                a = multiplication(a, float(input(zag)))
            elif dev == "/":
                a = division(a, float(input(zag)))
            elif dev == "**":
                a = exponentiation(a, float(input(zag)))
            elif dev == "/**":
                a = extracting(a)
            elif dev == "n!":
                a = factorial(a)
            elif dev == "":
                a = 0
                print("Калькулятор обнулён")
                break
            print(f"Итог: {a:g}")