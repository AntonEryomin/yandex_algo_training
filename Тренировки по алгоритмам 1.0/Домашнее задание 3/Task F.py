def solution(genom_a: str, genom_b: str) -> int:
    # все пары генома А
    gen_a_pairs = {}
    for idx in range(1, len(genom_a)):
        gen_pair = genom_a[idx-1:idx+1]
        if gen_pair in gen_a_pairs:
            gen_a_pairs[gen_pair] += 1
        else:
            gen_a_pairs[gen_pair] = 1

    # все пары генома B
    gen_b_pairs = {}
    for idx in range(1, len(genom_b)):
        gen_pair = genom_b[idx - 1:idx + 1]
        if gen_pair in gen_b_pairs:
            gen_b_pairs[gen_pair] += 1
        else:
            gen_b_pairs[gen_pair] = 1

    # Смотрим уникальные пары генов для генома А, если такая же пара есть в геноме Б, тогда мы добавляем к паре сходства
    common_gens = 0
    for k, v in gen_a_pairs.items():
        if k in gen_b_pairs:
            common_gens += v
    return common_gens


if __name__ == "__main__":
    genom_a = input()
    genom_b = input()

    print(solution(genom_a, genom_b))
