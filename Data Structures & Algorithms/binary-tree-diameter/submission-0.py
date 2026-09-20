# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_d=0
        def h(node):
            if not node :
                return 0
            rightf=h(node.right)
            leftf=h(node.left)
            self.max_d=max(self.max_d,rightf+leftf)
            return 1+max(leftf,rightf)

        h(root)
        return self.max_d