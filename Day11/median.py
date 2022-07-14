class Solution:
    def findMedianSortedArrays(self, array1, array2) -> float:
        array1[:] = sorted(array1+array2)
        array2.clear()
        if len(array1) % 2 == 0:
            p = int(len(array1)/2)
            m = (array1[p]+array1[p-1])/2
            if m % 2 == 0.0 or m % 2 == 1.0:
                return int(m)
            else:
                return m
        else:
            p = int(len(array1)/2)
            return array1[p]
