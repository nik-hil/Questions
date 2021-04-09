# https://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/
class newNode: 
  
    # Construct to create a new node 
    def __init__(self, key): 
        self.data = key
        self.left = None
        self.right = None
  
def isSumProperty(node: newNode):
    left = right = 0
    if not node.left and node.right:
        return node.data
    if node.left:
        left = isSumProperty(node.left)
    if node.right:
        right = isSumProperty(node.right)
    node.data = left + right + node.data
    return node.data
# Driver Code 
if __name__ == '__main__':
    root = newNode(50)
    root.left     = newNode(7)
    root.right     = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.left = newNode(1)
    root.right.right = newNode(30)
  
    isSumProperty(root)

