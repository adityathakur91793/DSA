class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, rght = 1, num

        while left <= rght:
            mid = (left + rght) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                rght = mid - 1

        return False