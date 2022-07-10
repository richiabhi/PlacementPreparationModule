class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> mp = new HashMap<>();
        Node t = head;

        while (t != null) {
            int val = t.val;
            Node temp = new Node(val);
            mp.put(t, temp);
            t = t.next;
        }

        Node root = mp.get(head);
        t = root;
        while (head != null) {
            t.next = mp.get(head.next);
            t.random = mp.get(head.random);
            t = t.next;
            head = head.next;
        }
        return root;
    }
}