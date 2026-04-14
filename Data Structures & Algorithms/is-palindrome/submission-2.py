class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newStr = ''

        for char in s:
            if char.isalnum():
                newStr += char
        reverseStr = newStr[::-1]

        if reverseStr.lower() != newStr.lower():
            return False
        else:
            return True