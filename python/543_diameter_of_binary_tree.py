from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]

        def longest_path(node) -> int:
            # DFS
            if not node:
                return 0

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter[0] = max(diameter[0], left_path + right_path)
            return 1 + max(left_path, right_path)

        longest_path(root)
        return diameter[0]
