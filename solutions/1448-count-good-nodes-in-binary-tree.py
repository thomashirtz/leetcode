class Solution:
    def goodNodes(self, root):
        self.answer = 0
        def dfs(node, previous_max):
            if node:
                if node.val >= previous_max:
                    self.answer += 1
                dfs(node.left, max(node.val, previous_max))
                dfs(node.right, max(node.val, previous_max))
        dfs(root, root.val)
        return self.answer