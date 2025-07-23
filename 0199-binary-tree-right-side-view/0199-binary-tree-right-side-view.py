# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        queue = deque()

        if not root:
            return []

        queue.append(root)
        #[root] 는 그냥 리스트임/
        result= []
        while queue:
            level_size = len(queue)
            

            for i in range(level_size):
                node = queue.popleft()
                
                if i == level_size -1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
        
        