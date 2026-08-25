def _wildcard_patterns(word: str):
    for i in range(len(word)):
        yield word[:i] + "*" + word[i + 1:]

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1

        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        if beginWord not in word_set:
            word_set.add(beginWord)

        pattern_to_words = defaultdict(list)
        for word in word_set:
            for pattern in _wildcard_patterns(word):
                pattern_to_words[pattern].append(word)

        step = 2
        begin_visited_words, end_visited_words = {beginWord}, {endWord}
        begin_word_queue, end_word_queue = deque([beginWord]), deque([endWord])

        while begin_word_queue:
            if len(begin_word_queue) > len(end_word_queue):
                begin_word_queue, end_word_queue = end_word_queue, begin_word_queue
                begin_visited_words, end_visited_words = end_visited_words, begin_visited_words

            for _ in range(len(begin_word_queue)):
                word = begin_word_queue.popleft()

                for pattern in _wildcard_patterns(word):

                    for nei_word in pattern_to_words[pattern]:
                        if nei_word in begin_visited_words:
                            continue

                        if nei_word in end_visited_words:
                            return step

                        begin_visited_words.add(nei_word)
                        begin_word_queue.append(nei_word)

                    pattern_to_words[pattern].clear()

            step += 1

        return 0
