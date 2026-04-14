class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        prev = [0] * n
        post = [0] * n

        prev[0] = 1
        post[n-1] = 1

        for i in range (1, n):
            prev[i] = prev[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            post[i] = post[i + 1] * nums[i + 1]

        for i in range(n):
            ans[i] = prev[i] * post[i]
        
        return ans

        