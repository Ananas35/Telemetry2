stroka = input("введите строку ")
slovo = []
number = 1
for qu in range(stroka.count(' ') + 1):
     slovo = stroka.split()
     if len(str(slovo)) <= 10:
         print(f" {number} {slovo [qu]}")
         number += 1
     else:
         print(f" {number} {slovo [qu] [0:10]}")
         number += 1