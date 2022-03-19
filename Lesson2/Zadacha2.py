liste = input("Введите значения в список: ").split()

for b in range(0, len(liste)-1, 2):
    liste[b], liste[b+1] = liste[b+1], liste[b]

print(liste)