# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head #current 초기화
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next #다음 노드로 이동
        return head