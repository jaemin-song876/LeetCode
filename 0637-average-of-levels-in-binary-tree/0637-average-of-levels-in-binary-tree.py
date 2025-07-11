# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        from collections import deque

        queue = deque()

        #put root node into queue
        if root is None:
            return[]

        queue.append(root)
        result=[]

        #bfs starts
        while queue:
            level_size=len(queue) #current level
            level_sum = 0

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            average = float(level_sum)/level_size
            result.append(average)

        return result