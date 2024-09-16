def summary():
    try:
        with open('5-file.txt', 'w') as object:
            line = input('Введите цифры через пробел \n')
            object.writelines(line)
            num = line.split()

            print(sum(map(int, num)))
    except IOError:
        print('Ошибка')
    except ValueError:
        print('Введите другие цифры')

summary()