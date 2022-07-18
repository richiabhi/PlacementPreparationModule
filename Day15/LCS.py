class Solution:
    def longestCommonPrefix(self, strs) -> str:
        def helper(n, arr):
            arr.sort(key=lambda x: len(x))
            res = ""
            prefix = arr[0]
            for i in range(len(prefix)):
                curr = arr[0][i]
                for j in range(1, n):
                    if arr[j][i] != curr:
                        return res
                res += curr
            return res
        return helper(len(strs), strs)
