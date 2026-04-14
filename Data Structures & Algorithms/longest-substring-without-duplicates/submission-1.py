class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        ans = 0

        left = 0
        right = 0

        while right < len(s):
            if s[right] not in window:
                window.add(s[right])
                right += 1
            else:
                window.remove(s[left])
                left += 1

            length = right - left

            ans = max(ans, length)

        return ans
