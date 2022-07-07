import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int x = 0, y = 0;

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for (y = 0; y < nums.length; y++) {

            if (map.containsKey(target - nums[y])) {
                x = map.get(target - nums[y]);
                return new int[] { x, y };
            }

            map.put(nums[y], y);
        }

        return new int[] { Integer.MIN_VALUE, Integer.MIN_VALUE };
    }
}