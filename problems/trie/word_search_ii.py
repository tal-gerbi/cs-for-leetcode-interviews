from abc import ABC, abstractmethod
from typing import List

from data_structures.trie.trie import Trie


class Solution(ABC):
    """
        - Title: Word Search II
        - Available at: https://leetcode.com/problems/word-search-ii/
        - Why was this chosen:
            A hard question involving a trie.
    """

    @abstractmethod
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass


class HashAndTrieSolution(Solution):
    """
    Approach:
        -Maintain a trie and a hash of all the remaining words
        -Recursively search for words from every cell (i, j) in range(m) x range(n)
        -Mark every visited cell to avoid using the same character twice.
        -If a word is found, remove it from the trie and from the hash.
        -Stop the recursion after the 10th character.

    Complexity:
        Time Complexity: O(m*n*4^10) = O(m*n)
        Space Complexity: O(k+m*n) (k is the number of words)
    """

    def _findWords(self, board: List[List[str]], currentWord: str, i: int, j: int,
                   wordsLeft: set[str], trie: Trie, visited: List[List[bool]]):
        if len(currentWord) == 10:
            return

        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m:
            return
        if j < 0 or j >= n:
            return
        if visited[i][j]:
            return
        currentWord += board[i][j]
        if not trie.startsWith(currentWord):
            return
        visited[i][j] = True

        if currentWord in wordsLeft:
            wordsLeft.remove(currentWord)
            trie.remove(currentWord)

        for deltaRows in [-1, 0, 1]:
            for deltaCols in [-1, 0, 1]:
                if deltaCols == 0 and deltaRows == 0:
                    continue
                if deltaCols != 0 and deltaRows != 0:
                    continue
                self._findWords(board, currentWord, i + deltaRows, j + deltaCols, wordsLeft, trie, visited)
        visited[i][j] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsLeft = set(words)
        trie = Trie()
        for word in words:
            trie.insert(word)

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                visited = [[False for _ in range(n)] for _ in range(m)]
                self._findWords(board, "", i, j, wordsLeft, trie, visited)
        return list(set(words) - wordsLeft)


def testBigExample():
    board = [
        ["o", "a", "a", "n"],
        ["e", "t", "a", "e"],
        ["i", "h", "k", "r"],
        ["i", "f", "l", "v"]
    ]
    words = ["oath", "pea", "eat", "rain"]
    assert set(HashAndTrieSolution().findWords(board, words)) == {"eat", "oath"}


def testSmallExample():
    board = [
        ["a", "b"],
        ["c", "d"]
    ]
    words = ["abcb"]
    assert HashAndTrieSolution().findWords(board, words) == []
