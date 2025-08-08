# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, node, min_val, max_val):
        #base case
        if not node:
            return True

        if not (min_val < node.val < max_val):
            return False

        left = self.validate(node.left, min_val, node.val)
        right = self.validate(node.right, node.val, max_val)

        return left and right