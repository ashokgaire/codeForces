class TrieNode:
    def  __init__(self):
        self.childern = [None]* 26
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _charToIndex(self,ch):
        return ord(ch) - ord('a')
    
    def insert(self,key):
        pCrawl = self.root

        lenght = len(key)

        for level in range(lenght):
            index = self._charToIndex(key[level])

            if not pCrawl.childern[index]:
                pCrawl.childern[index] = self.getNode()
            pCrawl = pCrawl.childern[index]

        pCrawl.isEndOfWord = True

    
    def search(self, key):

        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.childern[index]:
                return False
            pCrawl = pCrawl.childern[index]
        return pCrawl != None and pCrawl.isEndOfWord

def main():
  
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for key in keys:
        t.insert(key)
  
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
  
if __name__ == '__main__':
    main()