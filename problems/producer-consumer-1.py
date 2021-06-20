# https://docs.python.org/3/library/multiprocessing.html#exchanging-objects-between-processes

import time
from multiprocessing import Process, Queue

def put(q):
    for i in range(10):
        q.put(i)

def get(q):
    while not q.empty():
        print(q.get())
    return 

if __name__ == '__main__':
    q = Queue()
    prod = Process(target=put, args=(q,))
    prod.start()
    # print(q.get())    # prints "[42, None, 'hello']"
    consumer = Process(target=get,args=(q,) )
    time.sleep(1)
    consumer.start()
    prod.join()
    consumer.join()
