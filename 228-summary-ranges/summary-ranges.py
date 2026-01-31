class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        s = nums[0]

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] +1:
                if nums[i-1] == s:
                    res.append(str(s))
                else:
                    res.append(f"{s}->{nums[i-1]}")
                s = nums[i]

        if s == nums[-1]:
            res.append(str(s))
        else:
            res.append(f"{s}->{nums[-1]}")
            
        return res