class Solution {
    public String decodeString(String s) {
        Stack<Integer> counts = new Stack<>();
        Stack<StringBuilder> result = new Stack<>();
        StringBuilder currentString = new StringBuilder();
        int currentNum = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                currentNum = currentNum * 10 + (c - '0');
            } else if (c == '[') {
                counts.push(currentNum);
                result.push(currentString);
                currentString = new StringBuilder();
                currentNum = 0;
            } else if (c == ']') {
                StringBuilder temp = currentString;
                currentString = result.pop();
                int repeatCount = counts.pop();
                for (int i = 0; i < repeatCount; i++) {
                    currentString.append(temp);
                }
            } else {
                currentString.append(c);
            }
        }

        return currentString.toString();
    }
}
