# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr=head
        fast=ptr
        slow=ptr
        count=1
        prs=ptr
        while fast.next!=None:
            fast=fast.next
            
            if count>n:
                slow=slow.next
           
            count+=1
        if count==n and n==1 :
            head=head.next
           
        elif count==n-1:
             head.next=head.next.next
        elif count==n:
            head=head.next
        else:
            slow.next=slow.next.next
        return head