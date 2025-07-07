class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))

        #use the first row and first column to mark zero positions
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        
        #set elements to zero based on the first row and first column marks
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] ==0 :
                    matrix[i][j] = 0

        #set first row and first column to zero if they were marked
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0
