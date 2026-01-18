# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):
            if not node:
                return 0
            
            return max(depth(node.left), depth(node.right))+1

        def isBalance(node):
            if not node:
                return True
                
            length_r = depth(node.right)
            length_l = depth(node.left)

            diff = length_r - length_l

            if abs(diff) <= 1:
                balance = True
            else:
                balance = False

            return balance and isBalance(node.left) and isBalance(node.right)

        return isBalance(root)
        