class ListNode:
  def __init__(self,val,next=None):
    self.next = next
    self.val = val

  

def createNode():
  node = ListNode(1)
  current = node
  for i in range(2,6):
    current.next  = ListNode(i)
    current = current.next
  return node
  


def reveseNode(head):
  current = head

  while current.next != None:
    temp = current.next
    current.next = temp.next
    current = temp
  
  




head = createNode()
reveseNode(head)


