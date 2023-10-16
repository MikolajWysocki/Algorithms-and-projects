def dfs(root):
    if not root: return []
    return dfs(root.right) + [root.val] + dfs(root.left)