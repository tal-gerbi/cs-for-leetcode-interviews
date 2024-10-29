from abc import ABC, abstractmethod


class Solution(ABC):
    """
        - Title: Add Binary
        - Available at: https://leetcode.com/problems/add-binary/
        - Why was this chosen:
            A simple exercise with bit manipulation.
    """
    @abstractmethod
    def addBinary(self, a: str, b: str) -> str:
        pass


class LsbToMsbSolution(Solution):
    """
    Approach:
        Traverse the bits of both a and b from the least significant to the most significant.
        If the result is 2, set the carry to 1 and add it to the next pair or bits.

    Complexity:
        Time Complexity: O(|a|+|b|)
        Space Complexity: O(|a|+|b|)
    """

    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b

        n = len(a)
        res = [""] * n
        carry = 0
        for i in range(n-1, -1, -1):
            first = int(a[i])
            second = int(b[i])
            s = first + second + carry
            res[i] = str(s % 2)
            carry = s // 2
        if carry == 1:
            res = ["1"] + res

        return "".join(res)


def testFirstExample():
    assert LsbToMsbSolution().addBinary("11", "1") == "100"


def testSecondExample():
    assert LsbToMsbSolution().addBinary("1010", "1011") == "10101"
