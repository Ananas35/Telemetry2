import json

report = []
with open('7-file.txt', 'r') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_summa = 0
    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_summa += profit
    report.append(profits)
    report.append({'average_profit': (profit_summa / len(profits))})

with open('7-file.json.tmp', 'w') as json_file:
    json.dump(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)

print(f"Исходник:\n{text}\n")
print(f"Список:\n{report}\n")
print(f"json-объект:\n{json_report}")