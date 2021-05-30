class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        self.minimum = None
    
    def getMin(self):
        if self.top is None:
            return
        return self.minimum

    def peek(self):
        if self.top is None:
            return 
        else:
            if self.top.value < self.minimum:
                return self.minimum
            else:
                return self.top.value
    
    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            self.minimum = value
        
        elif value < self.minimum:
            temp = (2*value) - self.minimum
            new_node = Node(temp)
            new_node.next = self.top
            self.top = new_node
            self.minimum = value
        else:
            new_node= Node(value)
            new_node.next = self.top
            self.top = new_node
    
    def pop(self):
        if self.top is None:
            return
        else:
            removedNode = self.top.value
            self.top = self.top.next
            if removedNode < self.minimum:
                temp = self.minimum
                self.minimum = ((2*self.minimum) - removedNode)
                return temp
            else:
                return removedNode


stack = Stack()
 
stack.push(3)
stack.push(5)
print(stack.getMin())
stack.push(2)
stack.push(1)
print(stack.getMin())    
print(stack.pop())
print(stack.getMin())
print(stack.pop())
print(stack.peek())