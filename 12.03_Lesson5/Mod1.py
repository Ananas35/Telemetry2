import os

directoria = '/Users/meinwichtiges/PycharmProjects/telemetry/telemetry3/12.03_Lesson5'

def sozdanie():
    for l in range(1, 9):
        path = os.path.join(directoria, 'dir' + str(l))
        os.mkdir(path)
        print("Директория '% s' создана " % l)
def udalenie():
    for l in range(1, 9):
        path = os.path.join(directoria, 'dir' + str(l))
        os.rmdir(path)
        print("Директория '% s' удалена " % l)


udalenie()


















