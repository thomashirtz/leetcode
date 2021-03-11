class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1, t2):
        return self.recursif(t1, t2)

    def recursif(self, tree_left, tree_right):
        if not tree_left and not tree_right: return
        if not tree_left: tree_left = TreeNode(0)
        if not tree_right: tree_right = TreeNode(0)

        tree_left.left = self.recursif(tree_left.left, tree_right.left)
        tree_left.right = self.recursif(tree_left.right, tree_right.right)
        tree_left.val += tree_right.val

        return tree_left
