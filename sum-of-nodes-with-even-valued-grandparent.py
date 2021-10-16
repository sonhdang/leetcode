# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
    # General Idea:
    # - traverse BFS
    # - if current node is even:
    #     check grand children by checking children of both left and right
    # - else
    #     call sumEven Grandparent
        def sumEvenGrandparentRecursive(root):
            if root == None:
                return 0
            elif root.left == None and root.right == None:
                return 0
            else:
                evenSum = 0
                if root.val % 2 == 0:
                    if root.left != None:
                        if root.left.left != None:
                            evenSum += root.left.left.val
                        if root.left.right != None:
                            evenSum += root.left.right.val
                    if root.right != None:
                        if root.right.left != None:
                            evenSum += root.right.left.val
                        if root.right.right != None:
                            evenSum += root.right.right.val
                if root.left != None:
                    evenSum += sumEvenGrandparentRecursive(root.left)
                if root.right != None:
                    evenSum += sumEvenGrandparentRecursive(root.right)
            return evenSum
        return sumEvenGrandparentRecursive(root)