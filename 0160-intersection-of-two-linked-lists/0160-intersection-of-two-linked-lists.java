/**

 * Definition for singly-linked list.

 * public class ListNode {

 *     int val;

 *     ListNode next;

 *     ListNode(int x) {

 *         val = x;

 *         next = null;

 *     }

 * }

 */



public class Solution {

    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {

        if (headA == null || headB == null) {

            return null;

        }

        

        ListNode h1 = headA;

        ListNode h2 = headB;

        

        // Traverse both lists; upon reaching the end, switch to the other list's head

        while (h1 != h2) {

            h1 = (h1 == null) ? headB : h1.next;

            h2 = (h2 == null) ? headA : h2.next;

        }

        

        // Either the intersection node or null if no intersection

        return h1;

    }

}