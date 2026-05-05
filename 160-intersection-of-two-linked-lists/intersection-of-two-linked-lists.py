# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stackA = ['placeholder']
        stackB = ['placeholder2']

        while headA or headB:
            if headA != None:
                stackA.append(headA)
                headA = headA.next
            
            if headB != None:
                stackB.append(headB)
                headB = headB.next
            
        prev = None
        while stackA and stackB:
            itemA = stackA.pop()
            itemB = stackB.pop()

            if itemA != itemB:
                return prev

            prev = itemA
        return None