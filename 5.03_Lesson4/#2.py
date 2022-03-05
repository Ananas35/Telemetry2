with open('second.txt', 'r') as file:
    lines = file.readlines()
    print(f"Всего строк: {len(lines)}")
    for key, value in enumerate(lines):
        words = value.split(' ')
        print(f"Слов в строке {key + 1}: {len(words)}")