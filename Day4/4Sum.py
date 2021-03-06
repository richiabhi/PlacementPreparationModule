class Solution:
    def fourSum(self, arr, k):
        li = set()
        n = len(arr)
        arr.sort()
        for i in range(n-3):
            for j in range(i+1, n-2):
                l = j + 1
                r = n - 1
                while(l < r):
                    s = arr[i] + arr[j] + arr[l] + arr[r]
                    if (s == k):
                        li.add((arr[i], arr[j], arr[l], arr[r]))
                        l += 1
                        r -= 1
                    elif (s < k):
                        l += 1
                    else:
                        r -= 1
        return sorted(li)
