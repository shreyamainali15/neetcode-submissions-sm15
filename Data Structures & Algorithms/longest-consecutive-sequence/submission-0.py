class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()

        res = 0
        i = 0
        curr = 0
        seq = 0

        while i < len(nums):

            if curr != nums[i]:
                curr = nums[i]
                seq = 0
            while i < len(nums) and curr == nums[i]:
                i += 1
            
            curr += 1
            seq += 1

            res = max(res, seq)

        return res

        