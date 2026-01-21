class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        main = x 
        while x > 0:
            y = x%10
            res = res * 10 + y
            x = x // 10
        return main == res