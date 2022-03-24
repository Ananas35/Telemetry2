from threading import Thread, Semaphore
import random
from time import sleep

mainins = []
semofor = Semaphore(6)


def list(num):


     for n in range(num):
         inside = []

         def listins(limit):
             semofor.acquire()
             for i in range(limit):
                 x = round(random.uniform(1, 10))
                 inside.append(x)
                 i += 1
                 print(i)
                 print(inside)
                 sleep(0.3)
             semofor.release()
         potok_1 = Thread(target=listins, args=[5])
         potok_1.start()

         if potok_1.is_alive():
             potok_1.join()


         mainins.append(inside)
         n += 1
         print(n)
         print(mainins)
         sleep(0.3)

list(4)
