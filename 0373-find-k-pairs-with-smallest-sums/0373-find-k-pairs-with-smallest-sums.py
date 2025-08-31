import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        H=[]
        m,n=len(nums1), len(nums2)

        #initial
        for i in range(min(m,k)):
            total = nums1[i]+nums2[0]
            heapq.heappush(H,(total,i,0))

        res=[]

        while H and len(res) < k:
            total, i, j = heapq.heappop(H)
            res.append([nums1[i], nums2[j]])

            if j + 1 < n:
                nxt = nums1[i] + nums2[j+1]
                heapq.heappush(H,(nxt, i, j+1))

        return res
