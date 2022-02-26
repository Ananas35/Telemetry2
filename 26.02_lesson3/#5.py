result = 0
while True:
     line = input("Введите числа или символ '%' для выхода: ")
     tokens = line.split(" ")
     for token in tokens:
         try:
             num = float(token)
             result += num
         except:
             if token == '%':
                 print(f"Результат: {result}.")
                 exit(0)
             else:
                 print(f"Результат: {result}. ОШИБКА")
                 exit(1)
