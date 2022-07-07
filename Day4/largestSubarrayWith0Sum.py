class Solution:
    def maxLen(self, n, arr):
        ans = 0
        dic = dict()
        i = -1
        su = 0
        dic[su] = i
        while i < n-1:
            i += 1
            su += arr[i]
            if su not in dic:
                dic[su] = i
            else:
                l = i-dic.get(su)
                ans = max(ans,  l)
        return ans
