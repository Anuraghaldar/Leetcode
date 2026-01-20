class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.append(target)

        sort = sorted(nums)

        for i in range(len(sort)):
            if(sort[i] == target):
                return i
                break
 