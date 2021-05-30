class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def query(node):
    if node == None:
        return 0
    else:
        ldepth = query(node.left)
        rdepth = query(node.right)

        if ldepth > rdepth:
            return ldepth+1
        else:
            return rdepth +1

if __name__ == "__main__":
    t,x = map(int, input().split())
    node = Node(x)
    while t-1 > 0:
        pos = str(input())
        value = int(input())
        ptr = node

        for i in range(len(pos)):
            if pos[i] == 'L' and ptr.left != None:
                ptr = ptr.left
            elif pos[i] == 'R' and ptr.right != None:
                ptr = ptr.right
        if pos[-1] == 'L':
            ptr.left = Node(value)
        else:
            ptr.right = Node(value)
        
        ptr = node

        t -=1

print(query(node)+1)





