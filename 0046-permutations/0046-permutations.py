class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) ==1:
            return [nums[:]]

        result = []

        for _ in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)

            result.extend(perms)
            nums.append(n)
        return result

        