# https://leetcode.com/problems/same-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # qnodes = []
        # pnodes = []
        # preorder(p, qnodes)
        # preorder(q, pnodes)
        # return pnodes == qnodes
        return issame(p, q)


def issame(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False

    return issame(p.left, q.left) and issame(p.right, q.right)


def preorder(root, visited: list):
    if root is None:
        visited.append(None)
        return

    visited.append(root.val)
    preorder(root.left, visited)
    preorder(root.right, visited)
