class Solution:
    def longestPalindrome(self, S: str) -> str:
        start = 0
        end = 1
        for i in range(1, len(S)):
            l = i-1
            h = i
            while l >= 0 and h < len(S) and S[l] == S[h]:
                if h-l+1 > end:
                    start = l
                    end = h-l+1
                l -= 1
                h += 1

            l = i-1
            h = i+1
            while l >= 0 and h < len(S) and S[l] == S[h]:
                if h-l+1 > end:
                    start = l
                    end = h-l+1
                l -= 1
                h += 1
        return S[start:start+end]
