from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        x = n // 2
        res = Counter(nums)
        for k, v in res.items():
            if v > x:
                return k
