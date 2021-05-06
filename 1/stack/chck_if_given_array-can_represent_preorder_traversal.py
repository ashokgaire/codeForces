

INT_MIN = -2**32

def canRepresentBST(pre):
    s = []

    root = INT_MIN

    for value in pre:
        if value < root:
            return  False

        while (len(s) > 0 and s[-1] < value):
            root = s.pop()

        s.append(value)

    return True

# Driver Program
pre1 = [40 , 30 , 35 , 80 , 100]
print("true" if canRepresentBST(pre1) == True else "false")
pre2 = [40 , 30 , 35 , 20 ,  80 , 100]
print("true" if canRepresentBST(pre2) == True else "false")