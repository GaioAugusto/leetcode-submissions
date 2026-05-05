# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp != None:
            n += 1
            temp = temp.next
        
        temp1 = head
        temp2 = temp1
        # Move temp1
        for count1 in range(k-1):
            temp1 = temp1.next
        for count2 in range(n-k):
            temp2 = temp2.next

        value = temp1.val
        temp1.val = temp2.val
        temp2.val = value
        return head