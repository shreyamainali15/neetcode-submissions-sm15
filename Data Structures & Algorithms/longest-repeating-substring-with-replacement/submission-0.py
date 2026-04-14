class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        count = {}
        maxCount = 0
        res = 0

        while right < len(s):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            maxCount = max(maxCount, count[s[right]])

            right += 1

            while (right - left - maxCount) > k:
                count[s[left]] -= 1
                left +=1

            res = max(res, right - left)
        return res

        