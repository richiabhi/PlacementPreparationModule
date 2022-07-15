class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_ = Counter(nums)
        heap = []
        for ele in dict_:
            heappush(heap, (-dict_[ele], ele))
        res = []
        for i in range(len(heap)):
            if i >= k:
                break
            res.append(heappop(heap)[1])
        return res
