class Node:
    def  __init__(self,value):
        self.value =value
        self.left = None
        self.right = None

def inOrder(root):
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






root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
 
inOrder(root)