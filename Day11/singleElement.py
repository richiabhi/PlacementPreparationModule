class Solution:
    def singleNonDuplicate(self, nums) -> int:
        n = len(nums)
        l = 0
        r = n-1
        while l <= r:
            mid = l+(r-l)//2
            if mid % 2 == 0:
                if (mid < n-1) and (nums[mid] == nums[mid+1]):
                    l = mid+1
                elif (mid > 0) and (nums[mid] == nums[mid-1]):
                    r = mid-1
                else:
                    return nums[mid]
            if mid % 2 != 0:
                if(mid < n-1) and (nums[mid] == nums[mid+1]):
                    r = mid-1
                elif (mid > 0) and (nums[mid] == nums[mid-1]):
                    l = mid+1
                else:
                    return nums[mid]
