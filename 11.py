class Solution:
    def maxArea(self, height: list[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            leftLine = height[left]
            rightLine = height[right]
            if leftLine <= rightLine:
                area = (right - left) * leftLine
                left += 1
            else:
                area = (right - left) * rightLine
                right -= 1
            if area > res:
                res = area
        return res


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
