# bottom view of bst
# https://www.geeksforgeeks.org/bottom-view-binary-tree/

class Node: 
    
    def __init__(self, key): 
        
        self.data = key 
        self.left = None
        self.right = None

def bottomView(root, map, dist, level): 
    if not root:
        return
    if dist in map: 
        if level >= map[dist][1]: 
            map[dist] = [root.data, level] 
    else: 
        map[dist] = [root.data, level] 
    bottomView(root.left, map, dist-1,level+1)
    bottomView(root.right, map, dist+1, level+1)
 
        
if __name__=='__main__': 
    
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22) 
    root.left.left = Node(5) 
    root.left.right = Node(3) 
    root.right.left = Node(4) 
    root.right.right = Node(25) 
    root.left.right.left = Node(10) 
    root.left.right.right = Node(14) 
    
    print("Bottom view of the given binary tree :") 
    map = {}
    bottomView(root, map, dist=0,level=0) 
    for key in sorted(map.keys()):
        print(key, map[key])

    
