class Solution:
    operations_dispatch = {
        "+": lambda x, y: y + x,
        "-": lambda x, y: y - x,
        "*": lambda x, y: y * x,
        "/": lambda x, y: math.trunc(y / x),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for token in tokens:
            if token not in self.operations_dispatch:
                stack.append(int(token))
                continue
            stack.append(self.operations_dispatch[token](stack.pop(), stack.pop()))
        return stack[-1]