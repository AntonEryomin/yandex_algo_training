arr_size = int(input())
nums = list(map(int, input().split()))
num = int(input())


def get_nearest_num(nums: list, num: int) -> num:
    nearest_num = nums[0]
    for _ in nums:
        if abs(_ - num) < abs(nearest_num - num):
            nearest_num = _
    return nearest_num


print(get_nearest_num(nums, num))
