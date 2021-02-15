# Sum of two number in binary search tree

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

    while True:
        while done1 == False:
            if curr1:
                s1.append(curr1)
                curr1 = curr1.left
            else:
                if not s1:
                    done1 = 1
                else:
                    curr1 = s1.pop()
                    val1 = curr1.val
                    curr1 = curr1.right
                    done1 = 1
                    
        while done2 == False:
            if curr2:
                s2.append(curr2)
                curr2 = curr2.right
            else:
                if not s2:
                    done2 = 1
                else:
                    curr2 = s2.pop()
                    val2 = curr2.val
                    curr2 = curr2.left
                    done2 = 1
        print(val1, val2)
        if (val1 != val2)  and (val1 + val2) == target:
            print ("---", val1, val2)
            return True
        
        elif (val1 +val2) <target:
            done1 = False
        elif (val1 +val2) >target:
            done2 = False
        if val1 >= val2:
            return False
        
root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
find_pair(root, 21)
