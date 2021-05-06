def createStack():
    stck = []
    return stck

def isEmpty(stack):
    return len(stack) == 0

def push(stack,item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack) : print("stack underflow")
    else:
        return stack.pop()

def reverse(n):
    s = str(n)
    stack = createStack()
    for i in range(len(s)):
        push(stack,int(s[i]))

    for i in range(len(stack)):
        print(pop(stack), end="")


n = 86899
reverse(n)