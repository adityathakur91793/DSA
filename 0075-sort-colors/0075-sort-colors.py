class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        ans = 0
        right = len(nums) - 1

        while ans <= right:
            if nums[ans] == 0:
                nums[left], nums[ans] = nums[ans], nums[left]
                left += 1
                ans += 1

            elif nums[ans] == 2:
                nums[ans], nums[right] = nums[right], nums[ans]
                right -= 1

            else:
                ans += 1