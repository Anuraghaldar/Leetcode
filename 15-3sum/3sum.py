class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums [ i-1]:
                continue
            a = set()
            for j in range(i+1,len(nums)):
                k = -(nums[i] + nums[j])
                if (k in a):
                    res = tuple(sorted([nums[i], nums[j],k]))
                    result.add(res)
                a.add(nums[j])

        final = [list(t) for t in result]
        return final