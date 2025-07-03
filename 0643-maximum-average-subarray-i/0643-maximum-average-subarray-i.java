class Solution {
    public double findMaxAverage(int[] nums, int k) {
        // Step 1: Calculate the sum of the first 'k' elements
        int sum = 0;
        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        
        // Step 2: Initialize maxSum with the sum of the first 'k' elements
        int maxSum = sum;
        
        // Step 3: Slide the window across the array
        for (int i = k; i < nums.length; i++) {
            // Add the next element and remove the element going out of the window
            sum += nums[i] - nums[i - k];
            // Update maxSum if the new sum is larger
            maxSum = Math.max(maxSum, sum);
        }
        
        // Step 4: Return the maximum average
        return (double) maxSum / k;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Example 1
        int[] nums1 = {1, 12, -5, -6, 50, 3};
        int k1 = 4;
        System.out.println(solution.findMaxAverage(nums1, k1)); // Output: 12.75
        
        // Example 2
        int[] nums2 = {5};
        int k2 = 1;
        System.out.println(solution.findMaxAverage(nums2, k2)); // Output: 5.0
    }
}
