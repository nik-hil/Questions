# Better than this link
# https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/
class node:

    def __init__(self, x):
    
        self.data = x
        self.left = None
        self.right = None

def isSumTree(node):
    if not node:
        return 0
    ls = rt = 0
    if node.left: ls = isSumTree(node.left)
    if node.right: rt = isSumTree(node.right)
    if not node.left and not node.right:
        return node.data
    
    if  node.data == (ls + rt):
        return 2 * node.data
    else:
        return 0
    

# Driver code
if __name__ == '__main__':

    root = node(27)
    root.left= node(10)
    root.right = node(3)
    root.left.left = node(4)
    root.left.right = node(6)
    root.right.right = node(3)
    
    if(isSumTree(root)):
        print("The given tree is a SumTree ")
    else:
        print("The given tree is not a SumTree ")

