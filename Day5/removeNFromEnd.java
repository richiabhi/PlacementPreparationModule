class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode curr = head;
        ListNode point = head;
        while (curr != null) {
            curr = curr.next;
            if (n != -1) {
                n--;
            } else {
                point = point.next;
            }
        }
        if (n == -1) {
            point.next = point.next.next;
            return head;
        } else {
            return point.next;
        }

    }
}