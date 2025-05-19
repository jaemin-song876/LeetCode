# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        carry = 0

        while l1 or l2 or carry:#l1이나 l2가 아직 안끝났거나, carry가 남아있다면 계속 돌아!

            val1 = l1.val if l1 else 0
            # l1이 존재한다면, l1을, 없다면 0을 저장하기
            val2 = l2.val if l2 else 0

            total = val1+val2+carry
            carry = total //10 #몫
            digit = total % 10 #나머지

            curr. next = ListNode(digit)
            #방금 계산한 digit(자릿수)를 새 노드로 만들어서 저장하기
            curr = curr.next
            #포인터를 다음자리로 이동하기!

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            #l1, l2도 한 자리 앞으로 이동!

        return  dummy.next

