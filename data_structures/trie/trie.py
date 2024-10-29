class Trie:
    def __init__(self):
        self.next_chars = {}

    def insert(self, word: str) -> None:
        trie = self
        for ch in word + "_":
            if ch not in trie.next_chars:
                trie.next_chars[ch] = Trie()
            trie = trie.next_chars[ch]

    def search(self, word: str) -> bool:
        return self.startsWith(word + "_")

    def startsWith(self, prefix: str) -> bool:
        trie = self
        for ch in prefix:
            if ch not in trie.next_chars:
                return False
            trie = trie.next_chars[ch]
        return True

    @staticmethod
    def _remove(trie: 'Trie', prefix: str) -> bool:
        if prefix == "":
            return True

        ch = prefix[0]
        if ch not in trie.next_chars:
            raise Exception("word is not present is the trie")

        deleteNext = trie._remove(trie.next_chars[ch], prefix[1:])
        if not deleteNext:
            return False
        del trie.next_chars[ch]
        return len(trie.next_chars) == 0

    def remove(self, word: str):
        self._remove(self, word + "_")
