from typing import List, Dict, Set


def create_dictionary(words: List[str]) -> Dict[str, Set[str]]:
    dictionary = {}
    for word in words:
        if word.lower() in dictionary:
            dictionary[word.lower()].add(word)
        else:
            dictionary[word.lower()] = set([word])
    return dictionary


def mistake_counter(text: str, dictionary: Dict[str, Set[str]]) -> int:
    mistake_cnt = 0

    for word in text.split():
        if word.lower() in dictionary and word not in dictionary[word.lower()]:
            mistake_cnt += 1
        else:
            if len(''.join([ltr for ltr in word if ltr.isupper()])) != 1:
                mistake_cnt += 1
    return mistake_cnt


if __name__ == "__main__":
    words_in_dict = int(input())
    words_to_dict = []

    for _ in range(words_in_dict):
        words_to_dict.append(input())

    words_dictionary = create_dictionary(words_to_dict)
    text = input()

    mistake_nums = mistake_counter(text=text, dictionary=words_dictionary)
    print(mistake_nums)
