revenue = int(input('Какое значение выручки в рублях?: '))
costs = int(input('Какое значение издержек в рублях?: '))
profitability = round(((revenue - costs) / revenue) * 100, 2)

if revenue > costs:
    print('Поздравляю! Твоя фирма прибыльная')
    print(f'Рентабельность составила {profitability} % ({revenue - costs} руб.)')
    num_staff = int(input('Сколько сотрудников работает в фирме?: '))
    rev_one_staff = round(((revenue - costs) / num_staff), 2)
    print(f'Прибыль на одного сотрудника составляет {rev_one_staff} руб.')
else:
    print('У тебя убыточная фирма')