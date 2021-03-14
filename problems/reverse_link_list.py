# reverse link list
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    
def printNode(temp):
    while temp:
        print(temp.value)
        temp = temp.next

# Node1 -> Node2 -> Node3 -> Node4 -> Node5 -> Node6 -> Node7
# head = Node1

def reverseLL(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

def createLL():
    head = None
    for i in range(1,8):
        node = Node(i, None)
        if not head:
            head = node
            temp = node
        temp.next = node
        temp = node
    return head

head = createLL()
printNode(head)
head = reverseLL(head)
printNode(head)

