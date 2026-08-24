from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        # pattern -> all words matching that pattern
        pattern_to_words = defaultdict(list)

        for word in words | {beginWord}:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_to_words[pattern].append(word)

        # Bidirectional BFS
        begin_frontier = {beginWord}
        end_frontier = {endWord}

        begin_visited = {beginWord}
        end_visited = {endWord}

        distance = 1

        while begin_frontier and end_frontier:
            # Always expand the smaller frontier
            if len(begin_frontier) > len(end_frontier):
                begin_frontier, end_frontier = end_frontier, begin_frontier
                begin_visited, end_visited = end_visited, begin_visited

            next_frontier = set()

            for word in begin_frontier:
                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

                    for neighbor in pattern_to_words[pattern]:
                        if neighbor in end_visited:
                            return distance + 1

                        if neighbor not in begin_visited:
                            begin_visited.add(neighbor)
                            next_frontier.add(neighbor)

            begin_frontier = next_frontier
            distance += 1

        return 0