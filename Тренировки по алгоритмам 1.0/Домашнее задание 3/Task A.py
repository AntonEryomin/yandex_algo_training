from typing import List


def solution(nums: List[int]) -> int:
    unique_nums = set(nums)
    return len(unique_nums)


if __name__ == "__main__":
    # Считываем ввод
    nums = input().split(" ")

    # Выводим ответ
    print(solution(nums))

