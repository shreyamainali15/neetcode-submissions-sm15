class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = 0

        s1_count = {}
        s2_count = {}

        for char in s1:
            if char in s1_count:
                s1_count[char] += 1
            else:
                s1_count[char] = 1

        while right < len(s2):
            if s2[right] in s2_count:
                s2_count[s2[right]] += 1
            else:
                s2_count[s2[right]] = 1

            right += 1

            if (right - left) > len(s1):
                s2_count[s2[left]] -= 1

                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]

                left += 1

            if s1_count == s2_count:
                return True

        return False