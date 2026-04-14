class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        newSet = set(nums)

        length = 0

        for num in newSet:
            if num - 1 not in newSet:
                currLength = 1
                while (num + currLength) in newSet:
                    currLength += 1

                length = max(length, currLength)

        return length

        