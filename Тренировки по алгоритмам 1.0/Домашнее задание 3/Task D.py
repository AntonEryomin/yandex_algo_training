if __name__ == "__main__":
    unique_words = set()

    with open("input.txt") as f:
        for line in f:
            for word in line.strip().split(" "):
                if len(word) > 0:
                    unique_words.add(word)

    print(len(unique_words))
