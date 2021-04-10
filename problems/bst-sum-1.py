# Sum of two number in binary search tree
# https://stackoverflow.com/a/33441123/618018

class Node:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def find_pair(root, target):
    s1 = []
    s2 = []

    done1 = done2 = False
    val1 = val2 = 0
    curr1 = curr2 = root

    while s1 or s2 or curr1 or curr2:
        if curr1 or curr2:
            if curr1:
                s1.append(curr1)
                curr1 = curr1.left
            if curr2:
                s2.append(curr2)
                curr2 = curr2.right
        else:
            val =  s1[-1].val + s2[-1].val
            print(val, s1[-1].val , s2[-1].val )
            if val < target:
                curr1 = s1.pop()
                curr1 = curr1.right
            elif val == target:
                print("---> ", s1[-1].val, s2[-1].val)
                return
            else:
                curr2 = s2.pop()
                curr2 = curr2.left
            
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
find_pair(root, 23)
