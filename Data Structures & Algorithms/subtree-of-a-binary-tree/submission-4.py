# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def h(q,p):
            if not q and not p :
                return True 
            if not q or not p or q.val!=p.val:
                return False
            else :
                return h(q.right,p.right) and h(q.left,p.left)
        if not root:
            return False
        if h(root,subRoot):
            return True
        else:
            return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)