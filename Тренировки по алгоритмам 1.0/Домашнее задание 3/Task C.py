from typing import List


def solution(anya_nums: List[int], borya_nums: List[int]) -> List[str]:
    anya_colors = set(anya_nums)
    borya_colors = set(borya_nums)
    ans = []
    # одинаковые цвета
    intersection_colors = anya_colors.intersection(borya_colors)
    ans.append(str(len(intersection_colors)))

    # список общих цветов
    common_colors_list = " ".join([str(_) for _ in sorted(list(intersection_colors))])
    ans.append(common_colors_list)

    # цвета, которые есть только у Ани
    anya_unique_colors = anya_colors.difference(borya_colors)
    ans.append(len(anya_unique_colors))
    ans.append(" ".join([str(_) for _ in sorted(list(anya_unique_colors))]))

    # цвета, которые есть только у Бори
    borya_unique_colors = borya_colors.difference(anya_colors)
    ans.append(len(borya_unique_colors))
    ans.append(" ".join([str(_) for _ in sorted(list(borya_unique_colors))]))
    return ans


if __name__ == "__main__":
    anya_total_cubes, borya_total_cubes = [int(_) for _ in input().split(" ")]
    anya_cubes = []
    borya_cubes = []

    for _ in range(anya_total_cubes):
        anya_cubes.append(int(input()))

    for _ in range(borya_total_cubes):
        borya_cubes.append(int(input()))

    for _ in solution(anya_cubes, borya_cubes):
        print(_)
