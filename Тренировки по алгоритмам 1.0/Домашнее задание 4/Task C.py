from typing import List
from collections import Counter


def words_statistic(words: List[str]) -> str:
    words_counter = Counter(words)
    most_freaquent = 0
    for k,v in words_counter.items():
        most_freaquent = max(v, most_freaquent)

    top_words = [k for k, v in words_counter.items() if v == most_freaquent]
    return sorted(top_words)[0]


if __name__ == "__main__":
    words = []
    with open("input.txt") as f:
        for line in f:
            words += [word for word in line.strip().split(" ") if len(word) > 0]

    print(words_statistic(words))
