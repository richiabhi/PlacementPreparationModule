class Solution {
    public int maxSubArray(int[] nums) {
        int f = nums[0];
        int curr = nums[0];
        for (int i = 1; i < nums.length; i++) {
            curr = Math.max(nums[i], nums[i] + curr);
            f = Math.max(curr, f);
        }
        return f;
    }
}