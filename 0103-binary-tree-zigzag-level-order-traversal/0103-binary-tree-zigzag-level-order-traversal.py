# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        is_left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()

                if is_left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.insert(0,node.val)#list.insert(index, value) 지정한 인덱스 위치에 값을 삽입하겠다. 즉 리스트의 맨앞(0번위치)에 값을 넣겠다

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            is_left_to_right = not is_left_to_right

        return result