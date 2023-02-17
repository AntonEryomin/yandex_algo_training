from typing import List


def solution(allowed_nums: List[int], num: str) -> int:
    set_allowed_nums = set(allowed_nums)

    additional_buttons = set()
    for idx in range(len(num)):
        if int(num[idx]) not in set_allowed_nums:
            additional_buttons.add(int(num[idx]))

    return len(additional_buttons)


if __name__ == "__main__":
    allowed_nums = [int(_) for _ in input().split(" ")]
    num = str(input())

    print(solution(allowed_nums, num))
