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

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)

        diameter_l = self.diameterOfBinaryTree(root.left)
        diameter_r = self.diameterOfBinaryTree(root.right)

        diameter = max(diameter_l, diameter_r, depth_l + depth_r)

        return diameter
