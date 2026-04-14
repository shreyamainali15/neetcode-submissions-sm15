class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ind = {}
        
        for i, num in enumerate(nums):
            
            diff = target - num
            
            if diff in ind:
                return [ind[diff], i]
            
            ind[num] = i