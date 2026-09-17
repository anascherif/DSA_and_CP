# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def h(o):
            if not o:
                return
            
            h(o.left)
            h(o.right)
            res.append(o.val)
        h(root)
        return res