class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        res = 0
        i = 0
        for j in range(len(s)):
            if s[j] in dic:
                i = max(i, (dic[s[j]]+1))
            res = max(res, (j-i+1))
            dic[s[j]] = j
        return res
