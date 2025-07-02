class Solution {
    public int maxArea(int[] height) {
        int left = 0; // Initialize left pointer
        int right = height.length - 1; // Initialize right pointer
        int maxArea = 0; // Variable to store the maximum area

        // Move the pointers towards each other
        while (left < right) {
            // Calculate the area between the lines at left and right pointers
            int width = right - left;
            int minHeight = Math.min(height[left], height[right]);
            int area = width * minHeight;

            // Update the maximum area if the current area is larger
            maxArea = Math.max(maxArea, area);

            // Move the pointer pointing to the smaller line inward
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }

        return maxArea; // Return the maximum area
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        int[] height1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(solution.maxArea(height1)); // Output: 49

        // Example 2
        int[] height2 = {1, 1};
        System.out.println(solution.maxArea(height2)); // Output: 1
    }
}
