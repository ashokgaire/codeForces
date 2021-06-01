class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
 
 
def insert(root, key):
    if root is None:
        return Node(key)
    
    else:
        if root.val == key:
            return root
        
        
        elif key > root.val:
           root.right =  insert(root.right, key)
        else:
           root.left = insert(root.left, key)
    return root

def search(root,key):
    if root.val == key:
        print("present")
        return root
    elif key > root.val:
        search(root.right, key)
    else:
        search(root.left, key)
 
r = Node(50)
insert(r, 30)
insert(r, 20)
insert(r, 40)
insert(r, 70)
insert(r, 60)
insert(r, 80)
 
# Print inoder traversal of the BST
inorder(r)
search(r,30)