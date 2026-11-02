class Solution:
    def uprbond(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        ub = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                ub = mid
                high = mid - 1
            else:
                low = mid + 1

        return ub

    def lowrbond(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        lb = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                lb = mid
                high = mid - 1
            else:
                low = mid + 1

        return lb

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb = self.lowrbond(nums, target)

        if lb == -1 or nums[lb] != target:
            return [-1, -1]

        ub = self.uprbond(nums, target)

        if ub == -1:
            ub = len(nums) - 1
        else:
            ub -= 1

        return [lb, ub]