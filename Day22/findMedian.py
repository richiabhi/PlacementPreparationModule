from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        maxSize, minSize = len(self.maxHeap), len(self.minHeap)
        heappush(self.maxHeap, -1*num)
        if self.maxHeap and self.minHeap and (-1*self.maxHeap[0]) > self.minHeap[0]:
            heappush(self.minHeap, (-1*heappop(self.maxHeap)))

        if len(self.maxHeap) - minSize > 1:
            heappush(self.minHeap, (-1*heappop(self.maxHeap)))
        if len(self.minHeap) - maxSize > 1:
            heappush(self.maxHeap, -1*heappop(self.minHeap))

    def findMedian(self) -> float:
        maxSize, minSize = len(self.maxHeap), len(self.minHeap)
        if maxSize > minSize:
            return -1*self.maxHeap[0]
        if maxSize < minSize:
            return self.minHeap[0]
        if (maxSize+minSize) % 2 == 0:
            return (-1*self.maxHeap[0]+self.minHeap[0])/2
