# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        @lru_cache(None)
        def isInTree(root, node):

            if not root:
                return False
            val = root.val
            if  val==node:
                return True
            elif val > node:
                return isInTree(root.left, node)
            else:
                return isInTree(root.right, node)

        def isBothInTree(root, p, q):
            if isInTree(root, p) and isInTree(root, q):
                return True
            else:
                return False

        

        p1 = p.val
        q1 = q.val
        def parent_node(root, p, q):

            if isBothInTree(root, p, q):
                if isBothInTree(root.right, p, q):
                    return parent_node(root.right, p, q)
                elif isBothInTree(root.left, p, q):
                    return parent_node(root.left, p, q)
                else:
                    return root.val

        x = TreeNode(parent_node(root, p1, q1))
        return x


        