/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null) {
            return false; // empty list or single node cannot have cycle
        }

        ListNode slow = head;       // moves one step
        ListNode fast = head.next;  // moves two steps

        while (slow != fast) {
            if (fast == null || fast.next == null) {
                return false; // reached end => no cycle
            }
            slow = slow.next;
            fast = fast.next.next;
        }
        return true; // slow == fast means cycle detected
    }
}