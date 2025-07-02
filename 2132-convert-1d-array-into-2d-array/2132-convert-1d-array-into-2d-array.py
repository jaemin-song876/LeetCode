class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        if len(original) != m*n:
            return []
        
        for i in range(0,m):
            start = i*n
            end = start + n
            row = original[start:end]
            result.append(row)
        return result