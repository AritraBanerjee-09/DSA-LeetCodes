class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        np = {}

        for i in range(len(nums)):
            rmg = target - nums[i]

            if rmg in np:
                return [np[rmg], i]

            np[nums[i]] = i
        
        return []