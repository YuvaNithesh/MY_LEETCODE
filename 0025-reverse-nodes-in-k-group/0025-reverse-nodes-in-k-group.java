/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Dummy node to simplify edge cases
        ListNode dummy = new ListNode(0, head);
        ListNode prevGroup = dummy;
        
        while (true) {
            // Get the kth node from the current group's previous node.
            ListNode kth = getKthNode(prevGroup, k);
            if (kth == null) break; // If fewer than k nodes remain, we're done.
            ListNode nextGroup = kth.next;
            
            // Reverse the nodes in the current group.
            ListNode prev = kth.next;
            ListNode curr = prevGroup.next;
            while (curr != nextGroup) {
                ListNode temp = curr.next;
                curr.next = prev;
                prev = curr;
                curr = temp;
            }
            
            // Connect the previous group with the reversed group.
            ListNode temp = prevGroup.next;  // This is now the end of the reversed group.
            prevGroup.next = kth;
            prevGroup = temp;
        }
        
        return dummy.next;
    }
    
    // Helper method to get the kth node from the given starting node.
    private ListNode getKthNode(ListNode curr, int k) {
        while (curr != null && k > 0) {
            curr = curr.next;
            k--;
        }
        return curr;
    }
}
