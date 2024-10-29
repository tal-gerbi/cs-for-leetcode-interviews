from abc import ABC, abstractmethod

from data_structures.trie.trie import Trie


class Solution(ABC):
    """
        - Title: Implement Trie (Prefix Tree)
        - Available at: https://leetcode.com/problems/implement-trie-prefix-tree/
        - Why was this chosen:
            Implementing a trie is a no-brainer if one wants to understand this data structure.
    """
    @abstractmethod
    def insert(self, word: str) -> None:
        pass

    @abstractmethod
    def search(self, word: str) -> bool:
        pass

    @abstractmethod
    def startsWith(self, prefix: str) -> bool:
        pass


class PrefixTrieSolution(Solution):
    """
    Approach:
        Keep a map in every node, that maps the next character to the next node.

    Complexity:
        Time Complexity: Insert O(n); Search O(n); StartsWith O(n); Delete O(n)
        Space Complexity: Insert O(n); Search O(1); StartsWith O(1); Delete O(n) (can become O(1) with references to parents)
    """
    def __init__(self):
        self.trie = Trie()

    def insert(self, word: str) -> None:
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        return self.trie.search(word)

    def startsWith(self, prefix: str) -> bool:
        return self.trie.startsWith(prefix)


def testExample():
    trie = PrefixTrieSolution()
    trie.insert("apple")
    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")
    trie.insert("app")
    assert trie.search("app")
