# LRU Cache 
# Modified over https://leetcode.com/problems/lru-cache/discuss/46121/lru-cache-implementation-in-python-w-explanation


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, num=10):
        self.cache_limit = num
        self.cache = {}
        self.head = None
        self.tail = None
        
    def get(self, key):
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        if self.head == node:
            return node.val

        self.deleteNode(node)
        self.insertHead(node)

        return node.val

    def deleteNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        if next:
            next.prev = prev
        else:
            self.tail = prev
        
    def insertHead(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.next = self.tail
            self.tail.prev = self.head
            return
        self.head.prev = node
        node.prev = None
        node.next = self.head
        if self.tail == self.head:
            self.tail = self.head
            self.tail.next = None
        self.head = node
        

    def put(self, key, value):
        if self.cache_limit < len(self.cache):
            self.deleteNode(self.tail)
        node = Node(value)
        self.cache[key] = node
        self.insertHead(node)
            

    def printNode(self):
        temp = self.head
        if not self.head:
            print("Noting")
            return
        if (self.head == self.tail )and self.head:
            print(self.head.val)
            return
        
        while temp:
            print(temp.val, end=", ")
            temp = temp.next
        print()

cache = LRUCache(5)
cache.printNode()
cache.put(1,1)
cache.printNode()
cache.put(2,2)
cache.printNode()
cache.put(3,3)
cache.printNode()
cache.put(4,4)
cache.printNode()
cache.put(5,5)
cache.printNode()
cache.put(6,6)
cache.printNode()
cache.get(1)
cache.printNode()
cache.get(4)
cache.printNode()
