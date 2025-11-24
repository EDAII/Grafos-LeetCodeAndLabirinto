from collections import deque, defaultdict
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        parents = defaultdict(set)
        queue = deque([beginWord])
        visited = set([beginWord])
        found = False
        
        while queue and not found:
            next_level_visited = set()
            for _ in range(len(queue)):
                word = queue.popleft()
                word_chars = list(word)
                for i in range(len(word_chars)):
                    original_char = word_chars[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original_char:
                            continue
                        word_chars[i] = c
                        new_word = "".join(word_chars)
                        if new_word in word_set and new_word not in visited:
                            if new_word not in next_level_visited:
                                next_level_visited.add(new_word)
                                queue.append(new_word)
                            parents[new_word].add(word)
                            if new_word == endWord:
                                found = True
                    word_chars[i] = original_char
            visited |= next_level_visited
        
        if not found:
            return []
        
        res = []
        path = [endWord]
        
        def backtrack(word: str):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                path.append(p)
                backtrack(p)
                path.pop()
        
        backtrack(endWord)
        return res