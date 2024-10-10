from abc import ABC, abstractmethod


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


class ExampleSolution(Solution):
    """
    Approach:
        ___________

    Complexity:
        Time Complexity: _____
        Space Complexity: ____
    """

    def example(self) -> int:
        return 6


def test_example():
    assert ExampleSolution().example() == 6