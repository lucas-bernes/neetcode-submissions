# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        values = []
        while current:
            values.append(current.val)
            current = current.next

        index1=0
        index2=len(values)-1

        while index1<index2:
            if values[index1]!=values[index2]: return False
            index1+=1
            index2-=1

        return True