import java.util.*;

class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        Boolean[] zeroRow = new Boolean[m];
        Boolean[] zeroCol = new Boolean[n];
        Arrays.fill(zeroRow, Boolean.FALSE);
        Arrays.fill(zeroCol, Boolean.FALSE);
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (matrix[row][col] == 0) {
                    zeroRow[row] = true;
                    zeroCol[col] = true;
                }
            }
        }
        for (int row = 0; row < m; row++) {
            for (int col = 0; col < n; col++) {
                if (zeroRow[row] || zeroCol[col]) {
                    matrix[row][col] = 0;
                }
            }
        }
    }
}