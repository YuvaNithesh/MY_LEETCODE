import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxOperations(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;

        // Traverse through the array
        for (int num : nums) {
            int complement = k - num;

            // If the complement exists in the map, we can form a pair
            if (map.getOrDefault(complement, 0) > 0) {
                count++; // Found a pair
                map.put(complement, map.get(complement) - 1); // Decrement the complement's count
            } else {
                map.put(num, map.getOrDefault(num, 0) + 1); // Store the current number in the map
            }
        }

        return count; // Return the total count of pairs
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        int[] nums1 = {1, 2, 3, 4};
        int k1 = 5;
        System.out.println(solution.maxOperations(nums1, k1)); // Output: 2

        // Example 2
        int[] nums2 = {3, 1, 3, 4, 3};
        int k2 = 6;
        System.out.println(solution.maxOperations(nums2, k2)); // Output: 1
    }
}
