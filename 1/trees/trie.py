ALPHABET_SIZE = 26
indexs = 0

class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.childern = [None]*ALPHABET_SIZE
    

def insert(key, root):
    pcrawl = root

    for level in range(len(key)):
        index = ord(key[level]) - ord('a')
        if pcrawl.childern[index] == None:
            pcrawl.childern[index] = TrieNode()
        pcrawl= pcrawl.childern[index]
    pcrawl.isLeaf = True

def constructTrie(arr, n , root):
    for i in range(n):
        insert(arr[i], root)

def countChildern(node):
    count = 0
    for i in range(ALPHABET_SIZE):
        if node.childern[i] !=None:
            count +=1
            global indexs
            indexs = i
    return count


def walkTrie(root):
    pcrawl = root
    prefix = ""

    while(countChildern(pcrawl) == 1 and pcrawl.isLeaf == False):
        pcrawl = pcrawl.childern[indexs]
        prefix += chr(97+indexs)
    return prefix


def commonPrefix(arr, n, root):
    constructTrie(arr, n , root)
    return walkTrie(root)


n = 3
arr = ["flower","flow","flight"]
root = TrieNode()
print(commonPrefix(arr, n, root))