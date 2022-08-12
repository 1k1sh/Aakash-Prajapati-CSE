# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        anl=ListNode(1)
        temp2=0
        temp1=0
        ptr=anl
        while l1 and l2:
            temp2=(l1.val+l2.val+temp1)%10
            ptr.next=ListNode(temp2)
            ptr=ptr.next
            temp1=(l1.val+l2.val+temp1)//10
            l1=l1.next
            l2=l2.next
            
        if l2:
            l1=l2
        while l1:
            ptr.next=ListNode((l1.val+temp1)%10)
            ptr=ptr.next
            temp1=(l1.val+temp1)//10
            l1=l1.next
        if temp1!=0:
            ptr.next=ListNode(temp1)
            
        return anl.next