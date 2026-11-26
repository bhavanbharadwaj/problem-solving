# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        size = self.getListLength(curr)
        moves = size - n

        if size == n:
            return head.next
        
        curr = ListNode(-1, head)
        while moves > 0:
            curr = curr.next
            moves -= 1
        
        curr.next = curr.next.next
        return head

    
    def getListLength(self, node: Optional[ListNode]) -> int:
        count = 0
        while node:
            count += 1
            node = node.next
            
        return count