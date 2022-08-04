class Node:
   def __init__(self,data,next=None):
    self.data=data
    self.next=next
def print_ll(head):
    ptr=head
    while ptr:
        
        print(ptr.data)
        ptr=ptr.next   
    return head
    



  

n=Node(1,Node(2,Node(3,Node(4,Node(5)))))
print_ll(n)















































