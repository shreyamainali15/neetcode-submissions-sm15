class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        value = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in value:
                if stack and stack[-1] == value[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False
        