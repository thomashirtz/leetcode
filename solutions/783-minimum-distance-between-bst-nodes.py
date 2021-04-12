class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root):
        self.table = []

        def recursion(root):
            if root:
                self.table.append(root.val)
                recursion(root.left)
                recursion(root.right)

        recursion(root)
        self.table = sorted(self.table)
        answer = float('inf')
        for i in range(len(self.table)-1):
            answer = min(answer, abs(self.table[i+1] - self.table[i]))
        return answer