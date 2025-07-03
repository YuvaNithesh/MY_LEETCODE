import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();

        for (char ch : s.toCharArray()) {
            // Push opening brackets
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            }
            // For closing brackets, check matching
            else if (ch == ')' && !stack.isEmpty() && stack.peek() == '(') {
                stack.pop();
            } else if (ch == ']' && !stack.isEmpty() && stack.peek() == '[') {
                stack.pop();
            } else if (ch == '}' && !stack.isEmpty() && stack.peek() == '{') {
                stack.pop();
            }
            // No match or stack is empty
            else {
                return false;
            }
        }

        return stack.isEmpty(); // Stack must be empty for valid string
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isValid("()[]{}"));    // true
        System.out.println(sol.isValid("([{}])"));    // true
        System.out.println(sol.isValid("(]"));        // false
        System.out.println(sol.isValid("({[})"));     // false
    }
}
