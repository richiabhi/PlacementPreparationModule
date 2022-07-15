import heapq as h


def kthSmallLarge(arr, n, k):
    h.heapify(arr)
    temp = h.nlargest(k, arr)
    tmp = h.nsmallest(k, arr)
    return tmp, temp
