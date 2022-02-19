sezon_liste = ['Зима', 'Весна', 'Лето', 'Осень']
month_num = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
month = int(input("Введите порядковый номер месяца "))

if month ==1 or month == 12 or month == 2:
    print(sezon_liste[0])
if month ==1:
    print(month_num[0])
if month == 2:
    print(month_num[1])
if month ==12:
    print(month_num[11])

if month == 3 or month == 4 or month ==5:
    print(sezon_liste[1])
if month == 3:
     print(month_num[2])
if month == 4:
    print(month_num[3])
if month == 5:
    print(month_num[4])

if month == 6 or month == 7 or month == 8:
    print(sezon_liste[2])
if month == 6:
    print(month_num[5])
if month == 7:
    print(month_num[6])
if month == 8:
    print(month_num[7])

if month == 9 or month == 10 or month == 11:
    print(sezon_liste[3])
if month == 9:
    print(month_num[8])
if month == 10:
    print(month_num[9])
if month == 11:
    print(month_num[10])
elif month > 12:
       print("Такого месяца не существует")