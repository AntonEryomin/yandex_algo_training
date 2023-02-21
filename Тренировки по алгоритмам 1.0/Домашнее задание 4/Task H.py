def word_counter(target_word: str, sequence: str) -> int:
    # check if target_word longer than sequence
    if len(target_word) > len(sequence):
        return 0

    target_word_stats = dict()
    for _ in target_word:
        if _ in target_word_stats:
            target_word_stats[_] += 1
        else:
            target_word_stats[_] = 1
    cnt = 0

    # start base word
    base_word = dict()
    for _ in sequence[0:len(target_word)]:
        if _ in base_word:
            base_word[_] += 1
        else:
            base_word[_] = 1

    if base_word == target_word_stats:
        cnt += 1

    for idx in range(len(target_word), len(sequence)):
        # add new char
        if sequence[idx] in base_word:
            base_word[sequence[idx]] += 1
        else:
            base_word[sequence[idx]] = 1

        # delete prev char
        if base_word[sequence[idx-len(target_word)]] == 1:
            del base_word[sequence[idx-len(target_word)]]
        else:
            base_word[sequence[idx-len(target_word)]] -= 1

        # check if words equal
        if base_word == target_word_stats:
            cnt += 1
    return cnt


if __name__ == "__main__":
    tmp = input()
    target_word = str(input())
    sequence = str(input())

    print(word_counter(target_word=target_word, sequence=sequence))


