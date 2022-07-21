from collections import deque


class Solution:
    def rightSideView(self, root):
        q = deque([root])
        res = []
        while q:
            right = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                res.append(right.val)
        return res
