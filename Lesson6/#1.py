def cralya(q1, q2):
    result = 0
    try:
        result = q1 + q2
    except TypeError as error:
        result = f'{q1} или {q2} Переменная должна быть числом'
    finally:
        print('Программа завершена')

    return result


print(cralya(112, 243))

