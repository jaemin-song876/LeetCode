class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        triangle = [[1]]

        for i in range(1, numRows):
            prev = triangle[i-1]
            row = [1]

            for j in range(1, i):
                val = prev[j-1] +prev[j]
                row.append(val)

            row.append(1)
            triangle.append(row)

        return triangle

        