from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []
        x = len(nums)//3
        for k, v in dic.items():
            if v > x:
                ans.append(k)
        return ans
