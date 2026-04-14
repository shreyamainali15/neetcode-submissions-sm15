class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dummy = set()
        for num in nums:
            if num in dummy:
                return True
            dummy.add(num)
        return False