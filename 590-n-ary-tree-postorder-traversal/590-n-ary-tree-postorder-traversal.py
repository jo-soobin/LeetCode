"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.answer = []
        self.DFS(root)
        return self.answer
    
    def DFS(self, Node):
        if not Node:
            return
        for child in Node.children:
            self.DFS(child)
        self.answer.append(Node.val)
        