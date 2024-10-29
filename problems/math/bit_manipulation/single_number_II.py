from abc import ABC, abstractmethod
from typing import List


class Solution(ABC):
    """
        - Title: Single Number II
        - Available at: https://leetcode.com/problems/single-number-ii/
        - Why was this chosen:
            A non-binary representation is needed.
    """

    @abstractmethod
    def singleNumber(self, nums: List[int]) -> int:
        pass


class TrinaryXorSolution(Solution):
    """
    Approach:
        Traverse the trinary bits of both a and b from the least significant to the most significant.
        Add the (xor of the trinary bits (their sum modulo 3))*(3^(power index)) to the result.

    Complexity:
        Time Complexity: O(n)
        Space Complexity: O(1)
    """

    def singleNumber(self, nums: List[int]) -> int:
        nonZeroLeft = True
        power = 1
        res = 0
        while nonZeroLeft:
            nonZeroLeft = False
            s = 0
            for i, n in enumerate(nums):
                if n != 0:
                    nonZeroLeft = True
                s += n % 3
                nums[i] = n // 3
            res += (s % 3) * power
            power *= 3
        return res


def testFirstExample():
    assert TrinaryXorSolution().singleNumber([2, 2, 3, 2]) == 3


def testSecondExample():
    assert TrinaryXorSolution().singleNumber([0, 1, 0, 1, 0, 1, 99]) == 99
