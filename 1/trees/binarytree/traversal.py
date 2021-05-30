class Node:
    def  __init__(self,value):
        self.value =value
        self.left = None
        self.right = None

def height(root):
    if root == None:
        return 0
    else:
        lheght = height(root.left)
        rheight = height(root.right)

        if lheght > rheight:
            return lheght+1
        else:
            return rheight+1


def levelOrder(root, h):
    if root is None:
        return -1
    if h == 1:
        print(root.value, end= " ")
    else:
        levelOrder(root.left, h-1)
        levelOrder(root.right, h-1)

def printLevelOrder(root):
    h= height(root)
    for i in range(1,h+1):
        levelOrder(root, i)

def printPreorder(root):
    if root == None:
        return -1
    
    print(root.value, end = " ")
    printPreorder(root.left)
    printPreorder(root.right)

def printInorder(root):
    if root == None:
        return -1
    
    printInorder(root.left)

    print(root.value, end = " ")
    printInorder(root.right)


def printPostorder(root):
    if root == None:
        return -1
    
    printInorder(root.left)
    printInorder(root.right)

    print(root.value, end = " ")

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# bfs
print("level order traversal")
printLevelOrder(root)

#dfs
print("Preorder traversal of binary tree is")
printPreorder(root)
 
print("\nInorder traversal of binary tree is")
printInorder(root)
 
print("\nPostorder traversal of binary tree is")
printPostorder(root)