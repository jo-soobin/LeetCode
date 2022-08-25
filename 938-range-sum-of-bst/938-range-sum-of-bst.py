# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def DFS(self, node,low,high):
        if not node:
            return 0
        myreturn = 0
        if node.val >= low and node.val <=high:
            myreturn += node.val
        myreturn += self.DFS(node.left,low,high)
        myreturn += self.DFS(node.right,low,high)
        return myreturn
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.DFS(root, low, high)
