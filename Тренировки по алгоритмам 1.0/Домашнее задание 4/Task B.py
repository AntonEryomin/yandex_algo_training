from typing import List


def words_counter(words: List[str]) -> List[int]:
    words_statistics = []
    words_counter_dict = {}

    for word in words:
        if len(word) > 0:
            if word not in words_counter_dict:
                words_statistics.append(0)
                words_counter_dict[word] = 1
            else:
                words_statistics.append(words_counter_dict[word])
                words_counter_dict[word] += 1
    return " ".join([str(_) for _ in words_statistics])


if __name__ == "__main__":
    words = []
    with open("input.txt") as f:
        for line in f:
            words += line.strip().split(" ")

    print(words_counter(words))
