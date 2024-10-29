from abc import ABC, abstractmethod


class Solution(ABC):
    """
        - Title: Pow(x, n)
        - Available at: https://leetcode.com/problems/powx-n/
        - Why was this chosen:
            Logarithmic power implementation.
    """
    @abstractmethod
    def myPow(self, x: float, n: int) -> float:
        pass


class LogarithmicSolution(Solution):
    """
    Approach:
        - If n is odd, compute x*pow(x, n-1)
        - If n is even, compute pow(x,n//2)^2
        - For a negative n, return 1 / pow(x, -n)

    Complexity:
        Time Complexity: O(log n)
        Space Complexity: O(log n)
    """

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            return 1

        if n & 1 == 1:
            return x * self.myPow(x, n-1)

        resSquareRoot = self.myPow(x, n//2)
        return resSquareRoot * resSquareRoot


def closeEnough(a: float, b: float):
    return abs(a-b) < 0.00000001

def testFirstExample():
    assert LogarithmicSolution().myPow(2, 10) == 1024


def testSecondExample():
    assert closeEnough(LogarithmicSolution().myPow(2.1, 3), 9.261)


def testThirdExample():
    assert LogarithmicSolution().myPow(2, -2) == 0.25
