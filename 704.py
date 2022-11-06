def recursiveSearch(left, right, nums, target):
    # Termination
    if left > right:
        return -1

    mid = (left + right) // 2

    # Base case
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return recursiveSearch(mid + 1, right, nums, target)
    else:
        return recursiveSearch(left, mid - 1, nums, target)


def search(nums: list[int], target: int) -> int:
    return recursiveSearch(0, len(nums) - 1, nums, target)


# print(search([-1, 0, 3, 5, 9, 12], 9))
print(search([-1, 0, 3, 5, 9, 12], 2))
# print(search([5], -5))
