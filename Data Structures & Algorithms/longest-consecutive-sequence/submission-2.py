class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 

        res = 0
        
        numSet = set(nums)

        for num in numSet:

            if num - 1 in numSet:
                continue
            else:
                currentNum = num
                length = 0
                while currentNum in numSet:
                    currentNum += 1
                    length +=1
                res = max(res, length)


        return res

        