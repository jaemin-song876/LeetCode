class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j = len(height)-1
        max_area=0

        while i<j:#two pointers
            h = min(height[i], height[j])
            width = j-i
            area = h * width
            max_area = max(max_area, area)

            if height[i] < height[j]:
                i+=1
            else:
                j-=1 
        return max_area
