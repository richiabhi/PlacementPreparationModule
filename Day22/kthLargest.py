import heapq


class Solution:
    def findKthLargest(self, arr, k: int) -> int:
        heapq.heapify(arr)
        tmp = heapq.nlargest(k, arr)
        return tmp[-1]
