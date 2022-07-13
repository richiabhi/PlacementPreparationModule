class Solution:
    def permute(self, nums):
        ans = list()

        def helper(index, arr):
            if index == len(arr):
                ans.append(arr.copy())
                return
            for i in range(index, len(arr)):
                arr[index], arr[i] = arr[i], arr[index]
                helper(index+1, arr)
                arr[index], arr[i] = arr[i], arr[index]
        helper(0, nums)
        return ans
