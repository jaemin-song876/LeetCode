# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        from collections import deque

        queue = deque()

        #put root node into queue
        if root is None:
            return 0
        
        queue.append((root,1))

        while queue:
            node, depth = queue.popleft()

            if node.left:
                queue.append((node.left, depth +1))
            if node.right:
                queue.append((node.right, depth +1))
            # 자식 노드가 없을때 leaf노드니까 이때 return!
            if node.left is None and node.right is None:
                return depth