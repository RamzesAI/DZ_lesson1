a = int(input('Сколько километров спортсмен пробежал в первый день, км?: '))
b = int(input('Какой результат необходим, км?: '))
count = 1
while a < b:
    a = a + a * 0.1
    count = count +1
print(f'На {count} день спортсмен достиг результата - не менее {b} км')