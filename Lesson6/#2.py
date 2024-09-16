def chislo(ch1, ch2):
        result = []
        if ch1 < ch2:
            for k in range(ch1, ch2 + 1):
                 result.append(k)
        elif ch1 > ch2:
            for k in reversed(range(ch2, ch1 + 1)):
                 result.append(k)

        return result

ch1 = input('Введите первое целое число: ')
ch2 = input('Введите второе целое число: ')
try:
        n = int(ch1)
        n1 = int(ch2)
        print(chislo(n, n1))
except TypeError as error:
        print(f'{ch1} или {ch2} Переменная должна быть числом')


