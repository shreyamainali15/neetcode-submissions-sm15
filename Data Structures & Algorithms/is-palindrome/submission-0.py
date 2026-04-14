class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr =''

        for char in s:
            if char.isalnum():
                newStr += char

        reverse = newStr[::-1]

        if newStr.lower() == reverse.lower():
            return True

        return False

        