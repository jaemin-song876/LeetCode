# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        inorder_results = []

        def traveler(node):
            if not node:
                return []
            #왼쪽으로 가야 큰 값임
            traveler(node.left)

            inorder_results.append(node.val)

            traveler(node.right)

        traveler(root)

        return inorder_results[k-1]
        