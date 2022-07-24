class Solution:
    def connect(self, root):
        if not root:
            return None
        self.contwo(root.left, root.right)
        return root

    def contwo(self, node1, node2):
        if not node1 or not node2:
            return
        node1.next = node2
        self.contwo(node1.left, node1.right)
        self.contwo(node1.right, node2.left)
        self.contwo(node2.left, node2.right)
