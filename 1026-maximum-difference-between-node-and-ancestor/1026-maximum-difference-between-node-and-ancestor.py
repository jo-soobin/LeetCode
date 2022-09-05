# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node, Ancestor):
        if not node:
            return -1
        if not Ancestor:
            Current = 0
        else:
            Current = max([abs(node.val - max(Ancestor)), abs(node.val - min(Ancestor))])
        LeftMax = self.DFS(node.left, Ancestor + [node.val])
        RightMax = self.DFS(node.right, Ancestor + [node.val])
        return max([Current, LeftMax, RightMax])
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.DFS(root, [])