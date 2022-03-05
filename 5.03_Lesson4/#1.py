nepusto = True
file = open('First.txt', 'w')
while nepusto:
    line = input()
    if line == '':
        nepusto = False
    else:
        file.write(line + '\n')
file.close()
#