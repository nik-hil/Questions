# https://docs.python.org/3/library/multiprocessing.html
import time
from multiprocessing import Process, Queue

def put(q):
    for i in range(100):
        time.sleep(.000001)
        q.put(i)

def get(i, q):
    while not q.empty():
        print(i, " : ", q.get(),)
        time.sleep(.01)
    return 

if __name__ == '__main__':
    q = Queue()
    prod = Process(target=put, args=(q,))
    prod.start()
    consumers = [Process(target=get, args=(i, q)) for i in range(4)]
    time.sleep(1)
    for c in consumers:
        c.start()
    prod.join()
    for c in consumers:
        c.join()
