class Solution(object):
    def minEleSearch(self, arr):
        n = len(arr)
        left = 0
        right = n-1
        while left <= right:
            if arr[left] <= arr[right]:
                return left
            mid = (left+right)//2
            prev = (mid+n-1) % n
            nex = (mid+1) % n
            if (arr[mid] <= arr[nex]) and (arr[mid] <= arr[prev]):
                return mid
            elif arr[left] <= arr[mid]:
                left = mid+1
            else:
                right = mid - 1
        return -1

    def binary_search(self, arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        idx = self.minEleSearch(nums)
        x = self.binary_search(nums, 0, idx-1, target)
        y = self.binary_search(nums, idx, len(nums)-1, target)
        return max(x, y)
