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

        st = [] #stack처럼 사용, 지나온 노드 기억
        res  = [] #방문 순서 담기

        while root or st: #root는 현재 보고 있는 노드
            while root: #왼쪽끝까지 가는중
                st.append(root) #root가 있으면 그걸 st에 저장함
                root = root.left
                #root.left가 없으면 root가 None이되니까 while 탈출함.

            root = st.pop() #돌아가기; st에서 꺼내기
            res.append(root.val)

            root = root.right

        return res

        