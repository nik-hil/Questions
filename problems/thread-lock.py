# https://www.educative.io/edpresso/what-are-locks-in-python

import time, queue
from threading import Thread , Lock

value = 10
lock = Lock()
def debit():
    global value
    for val in range(0,10000,10):
        # print("debit")
        with lock:
            value += val

def credit():
    global value
    for val in range(0,1000,20):
        # print("Credit")
        with lock:
            value += val

th1 = Thread(target=debit,args=())
th2 = Thread(target=credit,args=())
th1.start()
th2.start()
th1.join()
th2.join()
print(value)
