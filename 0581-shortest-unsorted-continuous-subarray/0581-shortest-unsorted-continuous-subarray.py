class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        left = -1
        right = -1
        
        #find the 1st out of order element from left
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                left = i
                break
            
        
        if left == -1:
            return 0

        for i in range(n-1 , 0 , -1):
            if nums[i]< nums[i-1]:
                right = i
                break
        
        #min and max
        mn = min(nums[left:right + 1])
        mx = max(nums[left:right + 1])

        #expand the left boundary
        while left>0 and nums[left - 1]> mn:
            left -= 1
        
        #expand the right boundary
        while right < n-1 and nums[right +1] < mx:
            right += 1
        
        return right - left+1