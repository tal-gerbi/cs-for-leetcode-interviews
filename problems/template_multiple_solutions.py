from abc import ABC, abstractmethod

import pytest


class Solution(ABC):
    """
        - Title: ______
        - Available at: ______
        - Why was this chosen:
            _________
    """
    @abstractmethod
    def example(self) -> int:
        pass


class FirstSolution(Solution):
    """
    Approach:
        ___________

    Complexity:
        Time Complexity: _____
        Space Complexity: ____
    """

    def example(self) -> int:
        return 6


class SecondSolution(Solution):
    """
    Approach:
        ___________

    Complexity:
        Time Complexity: _____
        Space Complexity: ____
    """

    def example(self) -> int:
        return 6


@pytest.mark.parametrize("solution", [FirstSolution(), SecondSolution()])
def test_example(solution: Solution):
    assert solution.example() == 6