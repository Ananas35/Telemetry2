dictionary = {"Eins": "Один", "Zwei": "Два", "Drei": "Три", "Vier": "Четыре", "Fünf": "Пять", "Sechs": "Шесть", "Sieben": "Семь", "Acht": "Восемь", "Neun": "Девять"}

text_de = ''
with open('4-file.txt', 'r') as file_de:
    text_de = file_de.read()

text_ru = text_de
for de, ru in dictionary.items():
    text_ru = text_ru.replace(de, ru)

with open('4-file.tmp', 'w') as file_ru:
    file_ru.write(text_ru)