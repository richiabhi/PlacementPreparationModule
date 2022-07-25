class Solution:
    def kthLargest(self, root, k):
        # your code here
        traversal = []

        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            traversal.append(root.data)
            inorder(root.right)
        inorder(root)
        traversal = traversal[::-1]
        return traversal[k-1]
