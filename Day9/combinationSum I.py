class Solution:
    def combinationSum(self, candidates, target: int):
        def helperFunction(index, arr, target, ds=[]):
            if index == len(arr):
                if target == 0:
                    ans.append(ds.copy())
                return
            if arr[index] <= target:
                ds.append(arr[index])
                helperFunction(index, arr, target-arr[index], ds)
                ds.pop()
            helperFunction(index+1, arr, target, ds)

        ans = []
        helperFunction(0, candidates, target)
        return ans
