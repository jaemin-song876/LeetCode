# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        result_route=[]
        def dfs(node, current_path):

            if not node:
                return []

            if not node.left and not node.right:
                result_route.append(current_path)
                return

            #왼쪽 자식 노드가 있으면 탐색
            if node.left:
                dfs(node.left, current_path + "->"+ str(node.left.val))

            if node.right:
                dfs(node.right, current_path + "->"+ str(node.right.val))

        if root:
            dfs(root, str(root.val))

        return result_route