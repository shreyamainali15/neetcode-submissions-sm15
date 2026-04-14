class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        res = 0
        
        numSet = set(nums)

        for num in numSet:

            if num - 1 not in numSet:
                length = 1
                currentNum = num

                while currentNum + 1 in numSet:
                    length += 1
                    currentNum +=1 

                res = max(res, length)

        return res

        