# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #.next 로 따라가며 방문했을때 이미 방문한 노드가 등장한다면 사이클이 존재한다는 뜻!!
        slow = head #거북이
        fast = head #토끼

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
        return False
""" Floyd’s Cycle Detection (토끼와 거북이 알고리즘) 핵심 아이디어

slow 포인터는 한 칸씩,
fast 포인터는 두 칸씩 앞으로 간다.

만약 사이클이 없다면:
fast 포인터가 언젠가 None을 만나서 끝나게 돼. 즉, 연결 리스트의 끝까지 가버리니까 slow랑 fast는 절대 만나지 않아.

만약 사이클이 있다면:
fast 포인터는 slow보다 빨리 사이클 안을 돌게 되고, 결국 같은 위치에서 만나게 돼."""

