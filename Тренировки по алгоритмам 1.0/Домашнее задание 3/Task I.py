from typing import List


def solution(schoolchild_languages: List[List[str]], schoolchild_nums: int):
    lang_stat = dict()

    for langs in schoolchild_languages:
        for lang in langs:
            if lang not in lang_stat:
                lang_stat[lang] = 1
            else:
                lang_stat[lang] += 1

    at_least_one = [k for k, v in lang_stat.items()]
    all_knows = [k for k, v in lang_stat.items() if v == schoolchild_nums]
    return [all_knows, at_least_one]


if __name__ == "__main__":
    schoolchild_nums = int(input())
    schoolchild_languages = []
    for _ in range(schoolchild_nums):
        languages = []
        languages_nums = int(input())
        for __ in range(languages_nums):
            languages.append(input())
        schoolchild_languages.append(languages)

    for _ in solution(schoolchild_languages, schoolchild_nums):
        print(len(_))
        for lng in _:
            print(lng)
