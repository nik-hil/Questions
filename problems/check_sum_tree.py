# https://www.geeksforgeeks.org/check-for-children-sum-property-in-a-binary-tree/
class newNode: 
  
    # Construct to create a new node 
    def __init__(self, key): 
        self.data = key
        self.left = None
        self.right = None
  
def isSumProperty(node: newNode):
    if not node.left and not node.right:
        return node.data
    left = right = 0
    if node.left:
        left = isSumProperty(node.left)
    if node.right:
        right = isSumProperty(node.right)
    if node.data == left+right:
        return node.data 
    return 0
        
# Driver Code 
if __name__ == '__main__':
    root = newNode(10) 
    root.left = newNode(8) 
    root.right = newNode(2) 
    root.left.left = newNode(3) 
    root.left.right = newNode(5) 
    root.right.right = newNode(2) 
    
  
    if isSumProperty(root):
        print("True")

  
