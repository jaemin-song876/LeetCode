class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []

        def dfs(current_subset, index):
            # 종료조건
            if index == len(nums):
                result.append(list(current_subset))
                return

            #nums[index]를 포함하는 경우
            current_subset.append(nums[index])
            dfs(current_subset, index+1)

            #되돌리기 후 포함하지 않는경우
            current_subset.pop()

            #두번째 선택
            dfs(current_subset, index+1)

        #재귀함수 호출
        dfs([], 0)

        return result