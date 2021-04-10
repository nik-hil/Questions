# https://www.pythoncentral.io/circular-queue/

class CircularQueue:

    #Constructor
    def __init__(self, size):
        self.head = 0
        self.tail = 0
        self.max_size = size
        self.queue = [] 

    #Adding elements to the queue
    def put(self,data):
        if len(self.queue) < self.max_size:
            self.queue.append(data)
            self.tail  = (self.tail+1) % self.max_size
            print("Put ", self.queue)    
        elif self.size < self.max_size:
            self.queue[self.tail] = data
            self.tail  = (self.tail+1) % self.max_size
            print("Put ", self.queue)
        else:
            print("Queue Full")
        
    def get(self):
        if self.size == 0:
            print("Queue empty")
        data = self.queue[self.head]
        self.head = (self.head+1) % self.max_size
        print("Get ", data, self.queue)
        
    @property
    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        else:
            return self.max_size - (self.head - self.tail)

q = CircularQueue(3)
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.get()
q.get()
q.get()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.get()
q.put(1)

