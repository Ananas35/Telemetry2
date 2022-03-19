
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a<b: min = a
else: min = b
if c<min: min = c
itog = a+b+c-min
print("Сумма 2 наибольших =",itog)