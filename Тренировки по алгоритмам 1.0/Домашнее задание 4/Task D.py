from typing import List


def keys_statistics(possible_presses: List[int], presses: List[int]) -> List[bool]:
    presses_statistics = [0]*len(possible_presses)
    for press in presses:
        presses_statistics[press] += 1

    is_broken = []
    for idx in range(1, len(presses_statistics)):
        if presses_statistics[idx] <= possible_presses[idx]:
            is_broken.append(False)
        else:
            is_broken.append(True)
    return is_broken


if __name__ == "__main__":
    kyes_num = int(input())
    possible_presses = [0] + [int(_) for _ in input().split(" ") if len(_) > 0]
    total_presses = int(input())
    sequence_presses = [int(_) for _ in input().split(" ") if len(_) > 0]
    for _ in keys_statistics(possible_presses, sequence_presses):
        if _ is True:
            print("YES")
        else:
            print("NO")
