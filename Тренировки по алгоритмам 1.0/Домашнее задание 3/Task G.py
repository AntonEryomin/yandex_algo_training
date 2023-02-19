# НЕВЕРНОЕ РЕШЕНИЕ

from typing import List


def solution(positions: List[List[int]], tortuses_nums: int) -> int:
    true_positions = set()
    for pos in positions:
        if pos[0] + pos[1] == tortuses_nums-1:
            possible_position = pos[1]+1
            true_positions.add(possible_position)

    return len(true_positions)


if __name__ == "__main__":
    tortuses_nums = int(input())
    tortuses_positions = []

    for _ in range(tortuses_nums):
        tortuses_positions.append([int(_) for _ in input().split(" ")])

    print(solution(tortuses_positions, tortuses_nums))