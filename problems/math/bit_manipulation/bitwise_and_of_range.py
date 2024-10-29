from abc import ABC, abstractmethod


class Solution(ABC):
    """
        - Title: Bitwise AND of Numbers Range
        - Available at: https://leetcode.com/problems/bitwise-and-of-numbers-range/
        - Why was this chosen:
            Requires an insight to solve.
    """
    @abstractmethod
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        pass


class LongestCommonPrefixSolution(Solution):
    """
    Approach:
        Let's say that p is the longest prefix of the binary representations of left and right.
        1. If p == left == right, the result is p.
        2. Otherwise, the result must be p. The reason for that is, that the next bit of left must be 0, and the next bit of right must be 1 (since left < right). Therefore, when traversing the range [left, right] and ANDing the result, the next bit will be 0 (it's 0 in left), and the bits afterwards will be 0 (when the next bit becomes 1, all the bits after it will be 0).

        Therefore, the answer is always the longest common prefix of the binary representations of left and right. Computer it and return it.

    Complexity:
        Time Complexity: O(max(log left, log right))
        Space Complexity: ____
    """

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shifts = 0
        while left != right:
            left //= 2
            right //= 2
            shifts += 1
        return left << shifts


def testFirstExample():
    assert LongestCommonPrefixSolution().rangeBitwiseAnd(5, 7) == 4


def testSecondExample():
    assert LongestCommonPrefixSolution().rangeBitwiseAnd(0, 0) == 0


def testThirdExample():
    assert LongestCommonPrefixSolution().rangeBitwiseAnd(1, 2147483647) == 0