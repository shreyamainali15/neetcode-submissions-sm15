class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dummy = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in dummy:
                return [dummy[diff], i]

            dummy[nums[i]] = i
        