import java.util.*;

class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        Map<String, Integer> rowMap = new HashMap<>();
        int count = 0;

        // Store each row as a string and its frequency in the map
        for (int i = 0; i < n; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < n; j++) {
                row.append(grid[i][j]).append(",");
            }
            rowMap.put(row.toString(), rowMap.getOrDefault(row.toString(), 0) + 1);
        }

        // Check if any column matches any row
        for (int j = 0; j < n; j++) {
            StringBuilder col = new StringBuilder();
            for (int i = 0; i < n; i++) {
                col.append(grid[i][j]).append(",");
            }
            count += rowMap.getOrDefault(col.toString(), 0);
        }

        return count;
    }
}
