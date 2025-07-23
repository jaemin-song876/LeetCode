# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        if not root:
            return []

        queue=deque()
        queue.append(root)
        result=[]

        #making parent list
        def record_parents(root):
            parent = {}
            #자식노드를 key로, 부모노드를 value로 저장
            queue=deque([root])

            while queue:
                node = queue.popleft()
                
                if node.left:
                    parent[node.left] = node
                    queue.append(node.left)

                if node.right:
                    parent[node.right] = node
                    queue.append(node.right)
            return parent

        def bfs_from_target(target, parent_map, k):
            visited= set()
            queue=deque([target])

            visited.add(target)
            distance=0

            while queue:
                if distance ==k:
                    return [node.val for node in queue]

                for _ in range(len(queue)):
                    node=queue.popleft()
                    for neighbor in (node.left, node.right, parent_map.get(node)):
                        if neighbor and neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)

                distance += 1

            return []

        parent_map = record_parents(root)
        result = bfs_from_target(target, parent_map, k)
        return result
