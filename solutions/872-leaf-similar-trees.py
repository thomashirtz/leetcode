class Solution:
    def leafSimilar(self, root1, root2):
        leaves= [[], []]
        def DFS(root, tree):
            if root.left:
                DFS(root.left, tree)
            if root.right:
                DFS(root.right, tree)
            if not root.right and not root.left:
                leaves[tree-1].append(root.val)
        DFS(root1, 1)
        DFS(root2, 2)
        return leaves[0] == leaves[1]