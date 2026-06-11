class Solution:
    def isValid(self, s: str) -> bool:
        dq = deque()
        openning_to_closing = {'(': ')', '[': ']', '{': '}'}
        for ch in s:
            if ch in openning_to_closing:
                dq.append(ch)
                continue

            if not dq:
                return False

            if openning_to_closing[dq.pop()] != ch:
                return False
        return not dq
