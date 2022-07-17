from collections import deque


class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)

        def leftsmaller(nums):
            stack = deque()
            res = []
            for i, val in enumerate(nums):
                while stack and val <= stack[-1][1]:
                    stack.pop()
                if not stack:
                    res.append(-1)
                else:
                    res.append(stack[-1][0])
                stack.append((i, val))
            return res

        def rightsmaller(nums):
            stack = deque()
            res = []
            for i in range(len(nums)-1, -1, -1):
                while stack and nums[i] <= stack[-1][1]:
                    stack.pop()
                if not stack:
                    res.append(n)
                else:
                    res.append(stack[-1][0])
                stack.append((i, nums[i]))
            return res[::-1]

        l, r = leftsmaller(heights), rightsmaller(heights)
        res = 0
        for i in range(n):
            res = max(res, (r[i]-l[i]-1)*heights[i])
        return res
