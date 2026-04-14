class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = set()
        ans = 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right += 1
            else:
                window.remove(s[left])
                left += 1
            ans = max(ans, right - left)
        return ans
        