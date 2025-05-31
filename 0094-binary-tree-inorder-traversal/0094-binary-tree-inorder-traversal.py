# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        st = [] #stack처럼 사용
        res  = [] #순회 결과

        while root or st:
            while root: #왼쪽끝까지 가는중
                st.append(root)
                root = root.left

            root = st.pop()
            res.append(root.val)

            root = root.right

        return res

        