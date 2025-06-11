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

        if not root:
            return 0
        
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()
            #큐에서 맨 앞 노드를 꺼냄

            if not node.left and not node.right: #node.left랑 node.right가 없으면 leaf node
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node. right:
                queue.append((node.right, depth +1))
        