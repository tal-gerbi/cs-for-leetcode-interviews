from typing import List, Optional

from data_structures.binary_tree.binary_tree import TreeNode


def _construct(arr: List[Optional[int]], i: int) -> Optional[TreeNode]:
    if i >= len(arr):
        return None

    left = _construct(arr, 2*i+1)
    right = _construct(arr, 2*i+2)
    if left is None and right is None and arr[i] is None:
        return None
    return TreeNode(arr[i], left, right)


def construct(arr: List[Optional[int]]) -> Optional[TreeNode]:
    return _construct(arr, 0)
