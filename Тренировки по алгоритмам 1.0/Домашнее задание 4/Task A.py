if __name__ == "__main__":
    synonyms = {}
    for _ in range(int(input())):
        words = input().split(" ")
        if words[0] not in synonyms:
            synonyms[words[0]] = words[1]
        if words[1] not in synonyms:
            synonyms[words[1]] = words[0]

    target_word = input()
    print(synonyms[target_word])
