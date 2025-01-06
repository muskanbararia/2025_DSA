/*
* https://leetcode.com/problems/symmetric-tree/description/
* Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
*/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */

/**
 * @param {TreeNode} left
 * @param {TreeNode} right
 * @return {boolean}
 */
var isInvert = function(left,right){
    if (!left && !right){
        return true
    }
    if (!left || !right){
        return false
    }
    return left.val == right.val && isInvert(left.right,right.left) && isInvert(left.left,right.right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    return isInvert(root.left,root.right)
    
};