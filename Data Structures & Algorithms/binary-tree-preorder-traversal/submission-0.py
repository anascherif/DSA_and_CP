# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def h(o):
            if not o:
                return
            res.append(o.val)
            h(o.left)
            
            h(o.right)
        h(root)
        return res