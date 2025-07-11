class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n=len(matrix)
        #transpose
        for i in range(n):
            for j in range(i+1, n):
                if j >i: #(늘 성립하므로 빼도됨)
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #reverse each row
        for row in matrix:
            row.reverse()