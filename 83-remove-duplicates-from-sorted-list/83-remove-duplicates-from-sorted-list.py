# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        processed = head
        
        while processed and processed.next:
            if processed.val == processed.next.val:
                processed.next = processed.next.next
            else:
                processed = processed.next
        
        return head