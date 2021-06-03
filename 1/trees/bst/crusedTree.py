import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def insertIntoBst(root, node):
    if node.value < root.value:
        if root.left == None:
            root.left = node
        else:
            insertIntoBst(root.left, node)
    else:
        if root.right == None:
            root.right = node
        else:
            insertIntoBst(root.right, node)

def createBst(a,n):
    root = Tree(a[0])

    for i in range(1,n):
        node = Tree(a[i])
        insertIntoBst(root,node)
    return root

def findCommonParent(root,x,y):
    if x < root.value and y < root.value:
        findCommonParent(root.left, x, y)
    elif x > root.value and y > root.value:
        findCommonParent(root.right, x, y)
    else:
        return root

def findmax(parent, x):
    ans = x

    while parent and parent.value != x:
        ans = max(ans, parent.value)
        if x < parent.value:
            parent = parent.left
        else:
            parent = parent.right
    return ans

def query(root,x,y):
    parent = findCommonParent(root,x,y)
    ans1 = findmax(parent,x)
    ans2 = findmax(parent,y)
    return max(ans1, ans2)


n = int(input())
a = list(map(int, input().split()))
root = createBst(a,n)

x,y = map(int, input().split())
ans = query(root,x,y)
print(ans)
