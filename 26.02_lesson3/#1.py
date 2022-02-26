def funkzia(x, y):
    try:
        a = x / y
        return a
    except ZeroDivisionError:
        return "y не может быть равен нулю"
    except ValueError:
        return "Ввелите только номер"

print(funkzia(int(input("Введите x = ")), int(input("Введите y = "))))