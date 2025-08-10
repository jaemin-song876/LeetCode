# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        result =[]
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if node.left:
                stack.append((node.left,path + "->"+ str(node.left.val)))

            if node.right:
                stack.append((node.right, path+"->"+str(node.right.val)))

            if not node.left and not node.right:
                result.append(path)
        return result
