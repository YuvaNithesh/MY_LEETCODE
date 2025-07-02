import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        List<Boolean> result = new ArrayList<>();
        int maxCandies = 0;

        // Find the maximum number of candies any kid currently has
        for (int candy : candies) {
            maxCandies = Math.max(maxCandies, candy);
        }

        // Determine if each kid can have the greatest number of candies
        for (int candy : candies) {
            result.add(candy + extraCandies >= maxCandies);
        }

        return result;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example 1
        int[] candies = {2, 3, 5, 1, 3};
        int extraCandies = 3;
        System.out.println(solution.kidsWithCandies(candies, extraCandies)); // Output: [true, true, true, false, true]

        // Example 2
        candies = new int[]{4, 2, 1, 1, 2};
        extraCandies = 1;
        System.out.println(solution.kidsWithCandies(candies, extraCandies)); // Output: [true, false, false, false, false]

        // Example 3
        candies = new int[]{12, 1, 12};
        extraCandies = 10;
        System.out.println(solution.kidsWithCandies(candies, extraCandies)); // Output: [true, false, true]
    }
}
