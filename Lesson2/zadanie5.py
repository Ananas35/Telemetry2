number = int(input("Введите номер: "))
liste = [6, 5, 4, 3, 2, 1, 0]
b = liste.count(number)
for element in liste:
     if b > 0:
         x = liste.index(number)
         liste.insert(x+b, number)
         break
     else:
         if number > element:
             y = liste.index(element)
             liste.insert(y, number)
             break
         elif number < liste[len(liste) - 1]:
             liste.append(number)
print(liste)