class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx={}

        for i, num in enumerate(nums):
            needed = target - num
            if needed in pair_idx:
                return [pair_idx[needed], i]
            pair_idx[num] =i

