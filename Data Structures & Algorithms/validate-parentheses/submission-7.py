class Solution:
    def isOpenningBracket(self, ch: str) -> bool:
        return ch == '(' or ch == '[' or ch =='{'

    def isValid(self, s: str) -> bool:
        dq = deque()
        for ch in s:
            if self.isOpenningBracket(ch):
                dq.append(ch)
                continue

            if not dq:
                return False

            top = dq.pop()
            if top == '(':
                if ch != ')':
                    return False
                continue
            if top == '[':
                if ch != ']':
                    return False
                continue
            if top == '{':
                if ch != '}':
                    return False
                continue
        return not dq
