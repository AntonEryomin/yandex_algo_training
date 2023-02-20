from typing import List


def pyramid_height(blocks: List[List[int]]) -> int:
    w_blocks = {}
    for block in blocks:
        if block[0] in w_blocks:
            w_blocks[block[0]].append(block[1])
        else:
            w_blocks[block[0]] = [block[1]]

    height = 0
    for w in sorted(w_blocks.keys()):
        height += max(w_blocks[w])
    return height


if __name__ == "__main__":
    blocks = []
    for _ in range(int(input())):
        blocks.append([int(_) for _ in input().split(" ")])

    print(pyramid_height(blocks))
