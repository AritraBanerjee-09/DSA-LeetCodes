class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        count = 0

        prefix_count = {0:1}

        for n in nums:
            prefix_sum += n
        

            remaining = prefix_sum - k

            if remaining in prefix_count:
                count += prefix_count[remaining]

            prefix_count[prefix_sum]  = prefix_count.get(prefix_sum ,0) +1
        
        return count