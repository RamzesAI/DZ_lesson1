a = int(input('Введите целое положительное число: '))

# основа для вычисления остатка от деления
base = 1

# принимаем что максимальной является последняя цифра
max = a % 10

while True:
    # перебираем цифры с конца, ищем максимальную
    b = int(((a % (base * 10)) - (a % base)) / base)
    if b > max:
        max = b
    base = base * 10
    # выходим когда остаток от деления вводимого числа равен ему
    if a % base == a:
        break
print(max)