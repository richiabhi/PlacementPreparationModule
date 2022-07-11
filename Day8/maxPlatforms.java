import java.util.*;

class Solution {
    public static int calculateMinPatforms(int arr[], int dep[], int n) {
        // Write your code here.
        int i = 0;
        int j = 0;
        Arrays.sort(arr);
        Arrays.sort(dep);
        int maxTrain = 0;
        int platform = 0;
        while (i < n && j < n) {
            if (arr[i] <= dep[j]) {
                maxTrain++;
                i++;
            } else {
                maxTrain--;
                j++;
            }
            platform = Math.max(platform, maxTrain);
        }
        return platform;
    }
}