# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)

        return 1 + max(depth_l, depth_r)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)

        if abs(depth_r - depth_l) > 1:
            return False
        
        balanced_l = self.isBalanced(root.left)
        balanced_r = self.isBalanced(root.right)

        if balanced_l and balanced_r:
            return True
        
        return False
