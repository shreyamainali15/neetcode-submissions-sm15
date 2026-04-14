class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ind = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in ind:
                return [ind[diff], i]
            
            ind[nums[i]] = i
