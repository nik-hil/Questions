# https://www.youtube.com/watch?v=C6r1fDKAW_o

class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.key = data 
        self.left = None
        self.right = None
  
# A function to find 
def KSmallest(node, k):
    arr = [0,0]
    inorder(node, arr, k)
    return arr[1]
    
def inorder(node, arr, k):
    if not node:
        
        return
    inorder(node.left, arr, k)
    arr[0] += 1
    if arr[0] == k:
        arr[1]= node.key
        return
    inorder(node.right, arr, k)
     
    
# A utility function to insert a new 
# node with given key in BST 
def insert(node, key):
      
    # If the tree is empty,
    # return a new node 
    if node == None:
        return Node(key) 
  
    # Otherwise, recur down the tree 
    if key < node.key: 
        node.left = insert(node.left, key)
    elif key > node.key: 
        node.right = insert(node.right, key)
  
    # return the (unchanged) node pointer 
    return node
  
# Driver Code
if __name__ == '__main__':
      
    # Let us create following BST 
    #         50 
    #       /    \ 
    #      30    70 
    #    /  \  /  \ 
    #   20 40 60 80 
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20) 
    insert(root, 40) 
    insert(root, 70) 
    insert(root, 60) 
    insert(root, 80) 
    for i in range(8):
        print(i, " : ",KSmallest(root, i)) 
