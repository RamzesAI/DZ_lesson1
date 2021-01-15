print('Это небольшая программа по переводу секунд в формат чч:мм:сс')
user_seconds = int(input('Укажи количество секунд для дальнейшего перевода: '))
hours = int(user_seconds / 3600)
minutes = int((user_seconds - hours * 3600) / 60)
seconds = (user_seconds - hours * 3600) - minutes * 60
print('Вот что получилось после перевода')
if minutes < 10 and seconds < 10:
    print(f'{hours}:0{minutes}:0{seconds}')
if minutes >= 10 and seconds < 10:
    print(f'{hours}:{minutes}:0{seconds}')
if minutes < 10 and seconds >= 10:
    print(f'{hours}:0{minutes}:{seconds}')
if minutes >= 10 and seconds >= 10:
    print(f'{hours}:{minutes}:{seconds}')
