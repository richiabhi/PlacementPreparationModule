import heapq as hq


def kMaxSumCombination(a, b, n, k):
    ans = []
    heap = []
    for i in range(n):
        for j in range(n):
            hq.heappush(heap, -1*(a[i]+b[j]))

    for i in range(k):
        ans.append(-1*heap[0])
        hq.heappop(heap)
    return ans
