class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        top=0
        bottom = len(matrix) -1
        left=0
        right=len(matrix[0])-1
        result = []

        while top <= bottom and left <= right:

            # 왼 ->오
            for i in range(left, right+1):
                result.append(matrix[top][i])

            #위 ->아래
            for i in range(top +1, bottom+1):
                result.append(matrix[i][right])

            #오->왼
            if left < right and top < bottom:
                for i in range(right-1,left -1, -1):
                    result.append(matrix[bottom][i])

            #아래->위
            if left < right and top < bottom:
                for i in range(bottom-1, top, -1):
                    result.append(matrix[i][left])

            top +=1
            bottom -= 1
            left += 1
            right -= 1

        return result


