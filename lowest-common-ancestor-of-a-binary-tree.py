# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root, p, q):
    
    def lca(root):
        ## Basecase
        if root == None:
            return None
        
        ## Recursive call
        resultLeft = None
        resultRight = None

        if root.left != None:
            resultLeft = lca(root.left)
        if root.right != None:
            resultRight = lca(root.right)
            
        if root.val == p.val or root.val == q.val:
            return root
        else:
            if resultLeft != None and resultRight != None:
                return root
            if resultLeft == None and resultRight != None:
                return resultRight
            elif resultLeft != None and resultRight == None:
                return resultLeft
            else:
                return None
    return lca(root)