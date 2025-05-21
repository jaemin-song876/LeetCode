# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 #현재 tail뒤에 있는 노드로 list1을 붙인다는 뜻
                list1 = list1.next#list1 포인터를 한칸 앞으로 이동
            else:
                tail.next = list2
                list2=list2.next
            tail= tail.next

        #남은 리스트를 이어줌
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next
        