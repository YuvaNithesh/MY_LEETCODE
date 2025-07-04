import java.util.Stack;

class MyQueue {
    private Stack<Integer> inStack;
    private Stack<Integer> outStack;

    public MyQueue() {
        inStack = new Stack<>();
        outStack = new Stack<>();
    }

    // Push element x to the back of queue
    public void push(int x) {
        inStack.push(x);
    }

    // Removes the element from in front of queue and returns it
    public int pop() {
        peek();  // Ensure outStack has the current elements
        return outStack.pop();
    }

    // Get the front element
    public int peek() {
        if (outStack.isEmpty()) {
            while (!inStack.isEmpty()) {
                outStack.push(inStack.pop());
            }
        }
        return outStack.peek();
    }

    // Returns whether the queue is empty
    public boolean empty() {
        return inStack.isEmpty() && outStack.isEmpty();
    }
}
