from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left is None and self.left is None:
            return f"{self.val}"
        return f"[{self.val} [{self.left}, {self.right}]]"
