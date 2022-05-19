# https://leetcode.com/problems/subtree-of-another-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return is_sub_tree(root, subRoot)


def is_sub_tree(s, t):
    if t is None:
        return True
    if s is None:
        return False

    if is_same_tree(s, t):
        return True

    return is_sub_tree(s.left, t) or is_sub_tree(s.right, t)


def is_same_tree(s, t):
    if s is None and t is None:
        return True
    if s is not None and t is not None and s.val == t.val:
        return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

    return False
