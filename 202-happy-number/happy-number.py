class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
                break
            
            seen.add(n)
            
            arr = [int(i) for i in str(n)]
            
            num = 0
            
            for j in range(len(arr)):
                num += arr[j] ** 2
                
            n = num 
        else:
            return True