import threading
from time import sleep
def mysum():
     global num
     k = 1
     txt = str(num)
     while myevent.is_set():
         kor = k*k
         num += k*k
         txt += " + " + str(kor)
         print(f'["{kor}"], {txt} = {num}')
         k += 1
         sleep(0.3)
print('Сумма целых чисел')
t = threading.Thread(target=mysum)
num=0
myevent = threading.Event()
myevent.set()
t.start()
sleep(2)
myevent.clear()
if t.is_alive():
     t.join()

print(f'Результат: {num}')