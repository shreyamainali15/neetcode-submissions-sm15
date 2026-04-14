class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1

        ans = 0

        while left < right:
            width = right - left
            length = min(heights[right], heights[left])

            area = width * length

            ans = max(area, ans)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return ans


        