from email.header import Header


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
    if head==None:
        return head
    if head.next==None:
        return head
    h2=reverse_ll(head.next)
    head.next.next=head
    head.next=None
    return(h2)
        


n=Node(1,Node(2,Node(3,Node(4,Node(5)))))


reverse_ll(n)
print(n)

  















































