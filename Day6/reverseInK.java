/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        int l = 0;
        ListNode node = head;
        while (node != null) {
            l++;
            node = node.next;
        }
        if (k <= 1 || l < k) {
            return head;
        }
        ListNode prev = null;
        ListNode curr = head;
        for (int i = 0; i < k; i++) {
            ListNode nxt = curr.next;
            curr.next = node;
            node = curr;
            curr = nxt;
        }
        head.next = reverseKGroup(curr, k);
        return node;

    }
}