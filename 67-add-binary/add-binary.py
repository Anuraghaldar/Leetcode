class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_num = int(a,2)
        b_num = int(b,2)

        r = a_num + b_num
        res = bin(r)
        return res[2:]