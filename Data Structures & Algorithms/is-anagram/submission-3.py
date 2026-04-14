class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        count1 = {}

        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        if count == count1:
            return True
        else:
            return False        