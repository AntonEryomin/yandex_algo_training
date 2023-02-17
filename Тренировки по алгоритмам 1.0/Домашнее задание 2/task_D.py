nums = list(map(int, input().split()))


def greater_than_neighbour(nums: list) -> int:
    counter = 0
    for idx in range(1, len(nums)-1):
        if nums[idx-1] < nums[idx] > nums[idx+1]:
            counter += 1
    return counter


print(greater_than_neighbour(nums))
