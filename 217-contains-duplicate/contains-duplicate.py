class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        duplicate = False
        for i in nums:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for key, value in dict.items():
            if value > 1:
                duplicate = True
                break
            else:
                duplicate = False

        if duplicate:
            return True
        else:
            return False