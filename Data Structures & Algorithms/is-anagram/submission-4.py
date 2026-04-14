class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}

        for char in s:
            if char in countS:
                countS[char] += 1
            else:
                countS[char] = 1

        countT = {}

        for char in t:
            if char in countT:
                countT[char] += 1
            else:
                countT[char] = 1

        if countS == countT:
            return True
        else:
            return False
        