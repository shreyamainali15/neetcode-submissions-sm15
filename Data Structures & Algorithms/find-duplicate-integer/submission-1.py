class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dummy = set()

        for num in nums:
            if num in dummy:
                return num
            dummy.add(num)
        
        