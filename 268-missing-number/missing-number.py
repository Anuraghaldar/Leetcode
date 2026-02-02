class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = []
        for i in range(n+1):
            a.append(i)

        for j in a:
            if j not in nums:
                return j