class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        
        // Count the frequency of each number in the array
        for (int num : arr) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        Set<Integer> occurrences = new HashSet<>();
        
        // Check if any frequency count is repeated
        for (int count : frequencyMap.values()) {
            if (!occurrences.add(count)) {
                return false;
            }
        }

        return true;
    }
}
