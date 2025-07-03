class Solution {
    public boolean increasingTriplet(int[] nums) {
        // Initialize two variables to represent the smallest and second smallest elements
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for (int num : nums) {
            if (num <= first) {
                // Update the smallest element
                first = num;
            } else if (num <= second) {
                // Update the second smallest element
                second = num;
            } else {
                // Found a number greater than both first and second
                return true;
            }
        }

        return false; // No increasing triplet found
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        int[] nums1 = {1, 2, 3, 4, 5};
        System.out.println(solution.increasingTriplet(nums1)); // Output: true

        // Example 2
        int[] nums2 = {5, 4, 3, 2, 1};
        System.out.println(solution.increasingTriplet(nums2)); // Output: false

        // Example 3
        int[] nums3 = {2, 1, 5, 0, 4, 6};
        System.out.println(solution.increasingTriplet(nums3)); // Output: true
    }
}
