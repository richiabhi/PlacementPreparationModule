def findSecondMinimumValue(self, root) -> int:
    leaf = set()

    def dfs(node):
        if not(node.left):
            leaf.add(node.val)
            return
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return -1 if(len(leaf) < 2) else sorted(list(leaf))[1]
