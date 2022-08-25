"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def DFS(self, Node):
        if not Node:
            return
        self.Answer.append(Node.val)
        for child in Node.children:
            self.DFS(child)
    def preorder(self, root: 'Node') -> List[int]:
        self.Answer = []
        self.DFS(root)
        
        return self.Answer