class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1

        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList.append(beginWord)

        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
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

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i + 1:]

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
