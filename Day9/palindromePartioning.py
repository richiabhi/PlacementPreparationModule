class Solution:
    def partition(self, s: str):
        def isPalindrome(st):
            return st == st[::-1]
        res = []

        def dfs(s, path):
            if len(s) == 0:
                res.append(path)
            for i in range(len(s)):
                if isPalindrome(s[:i+1]):
                    dfs(s[i+1:], path+[s[:i+1]])
        dfs(s, [])
        return res
