class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operator = {"-", "+", "/", "*"}

        for token in tokens:
            if token in operator:
                a = int(stack.pop())
                b = int(stack.pop())

                if token == "+":
                    c = a + b
                elif token == "-":
                    c = b - a
                elif token == "*":
                    c = b * a
                else:
                    c = b/a
                stack.append(c)
            else:
                stack.append(token)
        return int(stack[-1])
        