class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        str_ans = ""
        sorted_strs = sorted(s)
        a = sorted_strs[0]
        b = sorted_strs[-1]
        for i in range(min(len(a),len(b))):
            if(a[i] != b[i]):
                return str_ans
            str_ans += a[i]
        return str_ans