class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1

        if beginWord not in wordList:
            wordList.append(beginWord)

        pattern_to_words = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_to_words[pattern].append(word)

        adj_list = defaultdict(list)
        for pattern, words in pattern_to_words.items():
            for i, word in enumerate(words):
                adj_list[word].extend(words[:i] + words[i+1:])

        if endWord not in adj_list:
            return 0

        step = 2
        visited_words = {beginWord}
        word_queue = deque([beginWord])

        while word_queue:
            for _ in range(len(word_queue)):
                word = word_queue.popleft()

                for nei_word in adj_list[word]:
                    if nei_word in visited_words:
                        continue

                    if nei_word == endWord:
                        return step

                    visited_words.add(nei_word)
                    word_queue.append(nei_word)

            step += 1

        return 0
