class Solution:
    def Recur(self, Node, target):
        if not Node:
            return -1
        if Node.val == target.val:
            return Node
        if Node.left:
            RetNode = self.Recur(Node.left, target)
            if type(RetNode) == TreeNode:
                return RetNode
        if Node.right:
            RetNode = self.Recur(Node.right, target)
            if type(RetNode) == TreeNode:
                return RetNode
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        print(target.val)
        Answer = self.Recur(cloned, target)
        return Answer