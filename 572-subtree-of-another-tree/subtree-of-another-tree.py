# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
#         # a = True
#         def leaf_same(root, subRoot):
#             a = True
#             if subRoot == None and root== None:
#                 return False
#             elif (subRoot!=None and root ==None) or (subRoot==None and root !=None):
#                 return True
#             # elif subRoot == None:
#             #     return True
#             # elif root == None:
#             #     return True
#             elif subRoot.val == root.val:
#                 print(3, subRoot.val , root.val)
#                 return leaf_same(root.left, subRoot.left) and leaf_same(root.right, subRoot.right)
#             else:
#                 return leaf_same(root.left, subRoot) and leaf_same(root.right, subRoot)

#         return  not leaf_same(root, subRoot)
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     part = False
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:   
        

#         def isSame(a , b):
#             if  not a and not b:
#                 return 1
#             elif (a and not b) or (not a and b):
#                 return 0
#             elif a.val != b.val:
#                 return 0
#             else:
#                 return isSame(a.left, b.left) and isSame(a.right, b.right)


#         def leaf_same(root, subRoot):
#             if self.part:
#                 return
#             elif root  and isSame(root, subRoot):
#                 self.part = True
            
#             elif root:
#                 leaf_same(root.left, subRoot) 
#                 leaf_same(root.right, subRoot) 

#         leaf_same(root, subRoot)
#         return  self.part

class Solution:
    def isSubtree(self, root, subRoot):
        def hash_tree(node, store):
            if not node:
                return None

            left = hash_tree(node.left, store)
            right = hash_tree(node.right, store)

            h = (node.val, left, right)
            store.add(h)
            return h

        root_hashes = set()
        hash_tree(root, root_hashes)

        sub_hash = hash_tree(subRoot, set())
        return sub_hash in root_hashes

        