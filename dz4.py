a = int(input('Введите целое положительное число: '))
base = 1 # основа для вычисления остатка от деления
max = a % 10 # принимаем что максимальной является последняя цифра
while True:
    # перебираем цифры с конца, ищем максимальную
    b = int(((a % (base * 10)) - (a % base)) / base)
    if b > max:
        max = b
    base = base * 10
    if a % base == a: # выходим когда остаток от деления вводимого числа равен ему
        break
print(max)