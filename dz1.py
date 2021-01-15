name = input('Укажи свое имя: ')
surname = input('Укажи свою фамилию: ')
age = int(input('Сколько тебе лет?: '))

full_name = f'Твое полное имя {name} {surname}'
age_univ = age - 22
print(full_name)
if age <= 24:
    print('Скорее всего ты еще учишься')
else:
    print(f'Если ты обычный человек, то {age_univ} года назад отучился в университете')
