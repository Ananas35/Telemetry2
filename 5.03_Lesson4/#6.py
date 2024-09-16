import re

report = {}
with open('6-file.txt', 'r') as file:
    text = file.read()
    file.seek(0)
    for row in file:
        rows = row.split(': ')
        chasy = re.findall(r"\d+", rows[1])
        report.update({rows[0]: sum([int(i) for i in chasy])})

print(f"Исходник:\n{text}\n")
print(f"Словарь:\n{report}")