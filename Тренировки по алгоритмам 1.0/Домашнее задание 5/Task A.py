from typing import List


def find_nearest(nums_a: List[int], nums_b: List[int]) -> List[int]:
    nums_a_idx = 0
    nums_b_idx = 0
    min_values = [min(min(nums_a), min(nums_b)), max(max(nums_a), max(nums_b))]
    while nums_a_idx < len(nums_a) and nums_b_idx < len(nums_b):

        if abs(nums_a[nums_a_idx] - nums_b[nums_b_idx]) < abs(min_values[0] - min_values[1]):
            min_values = [nums_a[nums_a_idx], nums_b[nums_b_idx]]

        if nums_a[nums_a_idx] < nums_b[nums_b_idx]:
            nums_a_idx += 1
        else:
            nums_b_idx += 1

    return min_values


if __name__ == "__main__":
    input()
    nums_a = [int(_) for _ in input().split()]
    input()
    nums_b = [int(_) for _ in input().split()]

    ans = find_nearest(nums_a=nums_a, nums_b=nums_b)
    print(ans[0], ans[1])
