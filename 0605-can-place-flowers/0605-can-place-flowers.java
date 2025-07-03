class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0; // Count of flowers that can be planted
        int length = flowerbed.length;

        for (int i = 0; i < length; i++) {
            // Check if the current plot is empty and its neighbors (if any) are also empty
            if (flowerbed[i] == 0 
                && (i == 0 || flowerbed[i - 1] == 0) 
                && (i == length - 1 || flowerbed[i + 1] == 0)) {
                // Plant a flower here
                flowerbed[i] = 1;
                count++;

                // Early exit if we've planted enough flowers
                if (count >= n) {
                    return true;
                }
            }
        }

        return count >= n;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        int[] flowerbed1 = {1, 0, 0, 0, 1};
        int n1 = 1;
        System.out.println(solution.canPlaceFlowers(flowerbed1, n1)); // Output: true

        // Example 2
        int[] flowerbed2 = {1, 0, 0, 0, 1};
        int n2 = 2;
        System.out.println(solution.canPlaceFlowers(flowerbed2, n2)); // Output: false

        // Example 3
        int[] flowerbed3 = {0, 0, 1, 0, 0};
        int n3 = 2;
        System.out.println(solution.canPlaceFlowers(flowerbed3, n3)); // Output: true
    }
}
