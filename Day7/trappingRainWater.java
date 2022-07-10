class Solution {
    public int trap(int[] height) {
        int n = height.length;
        int[] left = new int[n + 1];
        int[] right = new int[n + 1];
        int ans = 0;
        left[0] = height[0];
        right[n - 1] = height[n - 1];
        for (int i = 1; i < n; i++) {
            left[i] = Math.max(left[i - 1], height[i]);
        }
        for (int j = n - 1; j >= 0; j--) {
            right[j] = Math.max(right[j + 1], height[j]);
        }
        for (int k = 0; k < n; k++) {
            ans += Math.min(left[k], right[k]) - height[k];
        }
        return ans;
    }
}