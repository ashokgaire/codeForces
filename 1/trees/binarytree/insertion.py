class newNode:
    def  __init__(self,value):
        self.value =value
        self.left = None
        self.right = None


def inorder(root):
    stack = []
    current = root

    while True:

        if current !=None:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            print(current.value, end=" ")
            current = current.right
        else:
            break



def insert(temp,key):
    if not temp:
        root = newNode(key)
        return
    q = []
    q.append(temp)

    while len(q):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = newNode(key)
            break
        else:
            q.append(temp.left)
        
        if not temp.right:
            temp.right = newNode(key)
            break
        else:
            q.append(temp.right)

if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(11)
    root.left.left = newNode(7)
    root.right = newNode(9)
    root.right.left = newNode(15)
    root.right.right = newNode(8)
 
    print("Inorder traversal before insertion:", end = " ")
    inorder(root)
 
    key = 12
    insert(root, key)
 
    print()
    print("Inorder traversal after insertion:", end = " ")
    inorder(root)
