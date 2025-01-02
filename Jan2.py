'''
https://leetcode.com/problems/binary-tree-inorder-traversal/description/

Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res= []
        def traverse(root):
            if not root:
                return None
            left = traverse(root.left)
            if left:
                res.append(left)
            res.append(root.val)
            
            right = traverse(root.right)
            if right:
                res.append(right)
        traverse(root)
        return res
        