from abc import ABC, abstractmethod
from typing import Optional

from data_structures.binary_tree.binary_tree import BinTreeNode
from tests.binary_tree.construct import construct


class Solution(ABC):
    """
        - Title: Kth Smallest Element in a BST
        - Available at: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
        - Why was this chosen:
            It demonstrates a nice use case of binary search trees.
    """

    @abstractmethod
    def kthSmallest(self, root: Optional[BinTreeNode], k: int) -> int:
        pass


class KthSmallestSolution(Solution):
    """
    Approach:
        Try to find the kth smallest element:
            -In the left subtree (but get the size of the left subtree on the way)
            -(If it's not there and) If k == leftSize + 1, return the root's value
            -Otherwise, look for the element in the right subtree with k - (leftSize + 1)

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(h)
    """

    def _sizeAndKthSmallest(self, root: Optional[BinTreeNode], k: int) -> (int, Optional[int]):
        if root is None:
            return 0, None
        if not root.left and not root.right:
            return 1, root.val if k == 1 else None

        leftSize, leftSmallest = self._sizeAndKthSmallest(root.left, k)
        rightSize, rightSmallest = self._sizeAndKthSmallest(root.right, k - (leftSize + 1))
        if k == leftSize + 1:
            return leftSize + rightSize + 1, root.val
        return leftSize + rightSize + 1, leftSmallest if leftSmallest else rightSmallest

    def kthSmallest(self, root: Optional[BinTreeNode], k: int) -> int:
        _, kthSmallest = self._sizeAndKthSmallest(root, k)
        return kthSmallest


def test_small_tree():
    root = construct([3, 1, 4, None, 2])
    assert KthSmallestSolution().kthSmallest(root, 1) == 1


def test_large_tree():
    root = construct([5, 3, 6, 2, 4, None, None, 1])
    assert KthSmallestSolution().kthSmallest(root, 3) == 3


def test_very_large_tree():
    root = construct(
        [31,30,48,3,None,38,49,0,16,35,47,None,None,None,2,15,27,33,37,39,None,1,None,5,None,22,28,32,34,36,None,None,43,None,None,4,11,19,23,None,
         29,None,None,None,None,None,None,40,46,None,None,7,14,17,21,None,26,None,None,None,41,44,None,6,10,13,None,None,18,20,None,25,None,None,
         42,None,45,None,None,8,None,12,None,None,None,None,None,24,None,None,None,None,None,None,9])

    assert KthSmallestSolution().kthSmallest(root, 1) == 6
