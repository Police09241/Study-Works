
def addition (a, b):
    return a + b

def subtraction (a, b):
    return a - b

def multiplication (a, b):
    return a * b

def division (a, b):
    return a / b

def exponentiation (a, i):
    return a**i

def extracting (a):
    return a**0.5

def factorial (n):
    # if n < 0:
    #     sign = -1
    # else:
    #     sign = 1
    # result = 1

    # for i in range(2, abs(n) + 1):
    #     result *= i

    # return sign * result
    if n < 0:
        raise ValueError("Число должно быть положительным")
    result = 1
    for i in range(2, n + 1):
        print("Print", i)
        result *= i
    return result

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
zag = "Введите число: "
a = float(input("Введите начально число: "))
while True:
    dev = input("Что вы хотите с ним сделать: ")
    if dev == "+":
        print(addition(a, float(input(zag))))
