class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums) 
        result = [0] * n
        pref = [0] * n
        post = [0] * n

        pref[0] = 1
        post[n-1] = 1

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]

        for i in range(n):
            result[i] = pref[i] * post[i]
        
        return result 
        