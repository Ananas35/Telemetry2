start = float(input('Введите расстояние, км : '))
finish = float(input('Введите конечную цель: '))
day = 1

if start > finish:
    print(day)
while True:
    if start <= 0 or finish <= 0:
        print('Введите результат больше нуля!')
    else:
        while start < finish:
            start = start + start/10
            day += 1
        print(f'На {day}-й день спортсмен пробежал не менее {finish} км.')
        break
