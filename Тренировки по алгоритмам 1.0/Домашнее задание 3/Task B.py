from typing import List


def solution(nums_1: List[int], nums_2: List[int]) -> List[int]:
    nums_1 = set(nums_1)
    nums_2 = set(nums_2)
    # Получаем список чисел, входящих в оба множества в отсортированном виде
    sorted_common_nums = sorted(list(nums_1.intersection(nums_2)))

    return " ".join([str(_) for _ in sorted_common_nums])


if __name__ == "__main__":
    # Считываем ввод
    nums_2 = [int(_) for _ in input().split(" ")]
    nums_1 = [int(_) for _ in input().split(" ")]

    # Выводим ответ
    print(solution(nums_1, nums_2))
