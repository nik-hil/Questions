# https://docs.python.org/3/library/threading.html

import time, queue
from threading import Thread 

def put(q):
    for i in range(100):
        time.sleep(0.00001)
        q.put(i)

def get(q, i ):
    while not q.empty():
        print(i, q.get())
        time.sleep(0.1)
    return

if __name__ == "__main__":
    q = queue.Queue()
    prd = Thread(target=put, args=(q,))
    cons = [Thread(target=get, args=(q,i)) for i in range(4)]
    prd.start()
    for c in cons:
        c.start()
    prd.join()
    for c in cons:
        c.join()
