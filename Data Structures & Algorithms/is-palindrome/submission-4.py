class Solution:
    def isPalindrome(self, s: str) -> bool:
        dummy = ''

        for char in s:
            if char.isalnum():
                dummy += char.lower()

        reverse = dummy[::-1]

        return reverse == dummy