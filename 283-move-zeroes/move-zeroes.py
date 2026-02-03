class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0

        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i += 1

        for j in range(n- len(nums)):
            nums.append(0)

    
        