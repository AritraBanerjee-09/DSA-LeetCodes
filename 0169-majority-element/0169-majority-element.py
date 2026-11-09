class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # freq = {}

        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        #     if freq[num] > len(nums) // 2:
        #         return num
        # return -1

        candidate = None
        count = 0

        for i in nums:
            if count == 0:
                candidate = i
            
            if i == candidate:
                count += 1
            else:
                count -= 1
        return candidate