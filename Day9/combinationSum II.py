class Solution:
    def combinationSum2(self, candidates, target: int):
        ans = []
        candidates.sort()

        def helper(index, arr, target, ds=[]):
            if target == 0:
                ans.append(ds.copy())
                return
            for i in range(index, len(arr)):
                if i > index and arr[i] == arr[i-1]:
                    continue
                if arr[i] > target:
                    break
                ds.append(arr[i])
                helper(i+1, arr, target-arr[i], ds)
                ds.pop()
        helper(0, candidates, target)
        return ans
