# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        c=1
        
        ptr=head
        while ptr.next!=None:
            ptr=ptr.next
            c+=1
        if k>=c:
            z=k%c
        else:
            z=k
        for i in range(z):
            ptr=head
            while ptr.next.next!=None:
                ptr=ptr.next
            x=ptr.next
            ptr.next=None
            x.next=head
            head=x
        return head
            
            