nums = list(map(int, input().split()))


def is_increase(nums: list) -> str:
    current_post = nums[0]
    for idx in range(1, len(nums)):
        if nums[idx] > current_post:
           current_post = nums[idx]
        else:
            return "NO"
    return "YES"

print(is_increase(nums))