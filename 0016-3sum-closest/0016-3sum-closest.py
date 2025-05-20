class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf') #초기에는 아무 숫자도 없으니
        for i in range(len(nums)-2):
            right=len(nums)-1
            left=i+1

            while left<right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest_sum - target):
                    closest_sum = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return closest_sum

