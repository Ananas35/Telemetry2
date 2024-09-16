with open('third.txt', 'r') as file:
    stipendia = []
    beda = []
    list = file.read().split('\n')
    for i in list:
        i = i.split(':')
        if int(i[1]) < 5000:
            beda.append(i[0])
        stipendia.append(i[1])
print(f'Стипендия меньше 5.000 {beda}, средняя стипендия  {sum(map(int, stipendia)) / len(stipendia)}')