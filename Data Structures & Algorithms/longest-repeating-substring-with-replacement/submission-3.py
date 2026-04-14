class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        max_count = 0
        ans = 0

        while right < len(s):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            max_count = max(max_count, count[s[right]])

            right += 1

            while(right - left - max_count) > k:
                count[s[left]] -= 1
                left += 1

            ans = max(ans, right - left)

        return ans