from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        max_vals = deque()
        ans = []
        i = j = 0
        n = len(nums)
        while(j < n):
            if len(max_vals) == 0:
                max_vals.append(nums[j])
            else:
                while len(max_vals) != 0 and max_vals[-1] < nums[j]:
                    max_vals.pop()
                max_vals.append(nums[j])
            if (j-i+1) < k:
                j = j+1
            elif (j-i+1):
                ans.append(max_vals[0])
                if nums[i] == max_vals[0]:
                    max_vals.popleft()
                i = i+1
                j = j+1
        return ans
