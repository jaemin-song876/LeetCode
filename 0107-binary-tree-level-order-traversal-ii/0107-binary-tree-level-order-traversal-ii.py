# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        queue = deque()
        if root is None:
            return []

        queue.append(root)
        result = []

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):

                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
            
        result.reverse()

        return result

            