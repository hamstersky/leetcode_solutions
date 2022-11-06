class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    triplet = [nums[i], nums[j], nums[k]]
                    if sum(triplet) == 0 and sorted(triplet) not in triplets:
                        triplets.append(sorted([nums[i], nums[j], nums[k]]))
        return triplets


# triplets = set(map(lambda x: tuple(sorted(x)), triplets))
s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))
