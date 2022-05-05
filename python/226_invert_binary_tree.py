# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)


def invert(root: TreeNode):
    if root is not None:
        invert(root.left)
        invert(root.right)

        tmp = root.right
        root.right = root.left
        root.left = tmp

    return root
