# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max_depth(root)


def max_depth(root):
    if root is None:
        return 0

    left = max_depth(root.left)
    right = max_depth(root.right)

    return 1 + max(left, right)


def bfs(root):
    if root is None:
        return 0

    level = 0
    q = [root]

    while q:
        for _ in range(len(q)):
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        level += 1


def iterative_dfs(root):
    """pre-order DFS iterative"""
    if root is None:
        return 0

    level = max_level = 1
    stack = [(root, level)]

    while stack:
        node, level = stack.pop()
        max_level = max(max_level, level)

        if node.left is not None:
            stack.append((node.left, level + 1))
        if node.right is not None:
            stack.append((node.right, level + 1))
    return max_level
