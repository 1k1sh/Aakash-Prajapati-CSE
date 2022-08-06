class Node:
   def __init__(self,data,next=None):
    self.data=data
    self.next=next
def print_ll(head):
    ptr=head
    while ptr:
        
        print(ptr.data)
        ptr=ptr.next   
def insert_inlast(head,data):
    ptr=head
    while ptr.next:
        ptr=ptr.next
    ptr.next=Node(data)
    
def insert_atfirst(head,data):
    ptr=head
    head=Node(data)
    head.next=ptr
    return head
    
def insert_at_kth(head,data,k):
    ptr=head
    count=1
    while count<k-1:
        ptr=ptr.next
        count+=1
    temp=ptr.next
    ptr.next=Node(data)
    ptr.next.next=temp
def reverse_ll(head):
    ptr=head
    if ptr.next==None:
        return
          

n=Node(1,Node(2,Node(3,Node(4,Node(5)))))
insert_inlast(n,9)
s=insert_atfirst(n,1)
insert_at_kth(s,10,4)
print_ll(s)


  















































