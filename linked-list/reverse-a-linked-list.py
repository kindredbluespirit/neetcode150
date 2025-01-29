# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ## O(1) space recommended, which means it must be done inplace

        if head == None:
            return None
        
        if head.next == None:
            return head
        
        left, mid, right = None, head, head.next

        while right != None:
            mid.next = left
            left, mid, right = mid, right, right.next
        
        mid.next = left
        return mid

