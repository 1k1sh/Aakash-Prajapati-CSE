# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans=ListNode(123)
        ptr,list1p,list2p=ans,list1,list2
        while list1p!=None and list2p!=None:
            if list1p.val<=list2p.val:
                
                
                ptr.next=ListNode(list1p.val)
                ptr=ptr.next
                list1p=list1p.next
            else:
                
                
                ptr.next=ListNode(list2p.val)
                ptr=ptr.next
                list2p=list2p.next
        if list2p!=None:
            list1p=list2p
        if list1p!=None:
            
            
            ptr.next=list1p
           
        
        return ans.next     