class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        n = len(nums)
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

            if freq[i] > n // 2:
                return i
        return -1

        