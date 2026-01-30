class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] in dict:
                if i - dict[nums[i]] <= k:
                    return True
            
            dict[nums[i]] = i
        return False
        
        
        
        # duplicate = False

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             duplicate = True
        #             break

        # if duplicate:
        #     return True
        # else:
        #     return False