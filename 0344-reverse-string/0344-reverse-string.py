class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s)-1
        while left < right:
            a = s[left]
            s[left] = s[right]
            s[right] = a
            left +=1
            right -=1