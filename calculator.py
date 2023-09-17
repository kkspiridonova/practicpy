import math

print('1. сложение')
print('2. вычитание')
print('3. умножение')
print('4. деление')
print('5. возведение в степень')
print('6. квадратный корень')
print('7. факториал')
print('8. синус')
print('9. косинус')
print('10. тангенс')
opt = 1
while (0 < opt <= 10):
    opt = int(input("Выберите опцию:"))
    match opt:
        case 1:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            num3 = num1 + num2
            print("Результат:", num3)
        case 2:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            num3 = num1 - num2
            print("Результат:", num3)
        case 3:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            num3 = num1 * num2
            print("Результат:", num3)
        case 4:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            if num2 == 0:
                print("Ошибка!")
            else:
                num3 = num1 / num2
                print("Результат:", num3)
        case 5:
            num1 = float(input("Введите число: "))
            num2 = float(input("Введите степень: "))
            if num1 == 0 and num2 < 0:
                print ("Ошибка!")
            else:
                num3 = num1 ** num2
                print("Результат:", num3)
        case 6:
            num1 = float(input("Введите число: "))
            if num1 < 0:
                print("Ошибка!")
            else:
                num3 = math.sqrt(num1)
                print("Результат:", num3)
        case 7:
            num1 = float(input("Введите число: "))
            if num1 < 0:
                print("Ошибка!")
            else:
                num3 = math.factorial(num1)
                print("Результат:", num3)
        case 8:
            num1 = float(input("Введите угол (в градусах): "))
            num3 = math.sin(math.radians(num1))
            print("Результат:", num3)
        case 9:
            num1 = float(input("Введите угол(в градусах): "))
            num3 = math.cos(math.radians(num1))
            print("Результат:", num3)
        case 10:
            num1 = float(input("Введите число: "))
            num3 = math.tan(math.radians(num1))
            print("Результат:", num3)




