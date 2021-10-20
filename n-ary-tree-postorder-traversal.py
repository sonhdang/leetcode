# https://leetcode.com/problems/n-ary-tree-postorder-traversal/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        def recursivePostorder(node, result):
            if not node:
                return
            for i in node.children:
                recursivePostorder(i, result)
            result.append(node.val)
        
        result = []
        recursivePostorder(root, result)
        return result

