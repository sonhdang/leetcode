# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#       General Idea
#       BFS, use a list of list to keep track of elements in each level
#       use an integer to keep track of which level it is at
#       the index of the list will contains all the nodes at that level
#       root will have index zero, all direct children of root will have index 1
       
#       Pseudocode
#       levelOrderRecursive(root, levelNodes, level)
#       basecase: if node is None:
#               return
#           else
#               levelNodes[level].append(root.val)
#       recursive call:
#           if left is not None
#               levelOrderRecursive(root.left, levelNodes, level + 1)
#           if right is not None
#               levelOrderRecursive(root.right, levelNodes, level + 1)
        def levelOrder_r(root, levelNodes, level):
            # Basecase
            if not root:
                return
            
            # Append node to the levelNodes
            if len(levelNodes) <= level:
                levelNodes.append([])
            levelNodes[level].append(root.val)
            
            # Recursive calls
            if root.left:
                levelOrder_r(root.left, levelNodes, level + 1)
            if root.right:
                levelOrder_r(root.right, levelNodes, level + 1)
        
        levelNodes = []
        levelOrder_r(root, levelNodes, 0)
        return levelNodes