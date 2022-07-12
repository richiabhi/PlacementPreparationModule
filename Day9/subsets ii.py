class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        ans = []

        def helper(index, arr, ds=[]):
            ans.append(ds.copy())
            for i in range(index, len(arr)):
                if i != index and arr[i] == arr[i-1]:
                    continue
                ds.append(arr[i])
                helper(i+1, arr, ds)
                ds.pop()
        helper(0, nums)
        return ans
