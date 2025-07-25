# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False

        if targetSum - root.val == 0 and not root.right and not root.left:
            return True

        left = self.hasPathSum(root.left, targetSum-root.val)

        right = self.hasPathSum(root.right, targetSum-root.val)

        if left or right:
            return True
        else:
            return False