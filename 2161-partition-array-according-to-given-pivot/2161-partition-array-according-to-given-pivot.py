class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        ans = [0] * len(nums)
        left = 0
        right = len(nums) - 1
        for i in range(len(nums)):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            if nums[len(nums) - 1 - i] > pivot:
                ans[right] = nums[len(nums) - 1 - i]
                right -= 1
        while left <= right:
            ans[left] = pivot
            left += 1

        return ans
