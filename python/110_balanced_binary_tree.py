from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        res, _ = get_height(root)
        return res


def get_height(root):
    if root is None:
        return True, 0

    L = get_height(root.left)
    R = get_height(root.right)
    is_balanced = L[0] and R[0] and abs(L[1] - R[1]) <= 1
    return is_balanced, 1 + max(L[1], R[1])
