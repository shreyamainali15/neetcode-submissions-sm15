class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count1 = {}

        for char in s1:
            if char in count1:
                count1[char] += 1
            else:
                count1[char] = 1

        left = 0 
        right = 0

        count2 = {}
        
        while right < len(s2):
            if s2[right] in count2:
                count2[s2[right]] += 1
            else:
                count2[s2[right]] = 1

            right += 1

            if (right - left) > len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]

                left += 1

            if count1 == count2:
                return True

        return False

            