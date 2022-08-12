# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        elif not head.next:
            return head
        ptr=ListNode(123,head)
        head=ptr
        while ptr.next!=None and ptr.next.next!=None:
            x=ptr.next
            ptr.next=x.next
            x.next=ptr.next.next
            ptr.next.next=x
            ptr=ptr.next.next
        return head.next
            