vyruchka = int(input('Введите выручку: '))
costen = int(input('Введите издержки: '))
rabotniki = int(input('Введите количество сотрудников: '))
geshaft = vyruchka - costen
rentable = geshaft / vyruchka
sal = geshaft / rabotniki
while True:
    if vyruchka > costen:
        print(f'Прибыль фирмы составила: {geshaft:.2f}')
        print(f'Соотношение прибыли к выручке: {rentable:.2f}')
        print(f'Прибыль на одного сотрудника: {sal:.2f}')
        break
    elif vyruchka < costen:
        print(f'Выручка меньше издержок : {geshaft:.2f},  Вы работаете в минус ;(')
        break
    else:
        print(f'Выручка и издержки равны, Вы работаете в ноль, прибыль равна {geshaft:.2f}.')
        break
