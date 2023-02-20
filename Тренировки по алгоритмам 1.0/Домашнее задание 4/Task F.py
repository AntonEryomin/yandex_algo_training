from typing import List


def purchase_stats(purchases: List[List[str]]) -> List[str]:
    buyers = {}
    for purchase in purchases:
        # name | goods | count
        if purchase[0] in buyers:
            if purchase[1] in buyers[purchase[0]]:
                buyers[purchase[0]][purchase[1]] += int(purchase[2])
            else:
                buyers[purchase[0]][purchase[1]] = int(purchase[2])
        else:
            buyers[purchase[0]] = {purchase[1]: int(purchase[2])}

    final_ans = []
    for buyer in sorted(buyers.keys()):
        final_ans.append(f"{buyer}:")
        for good in sorted(buyers[buyer].keys()):
            final_ans.append(f"{good} {str(buyers[buyer][good])}")

    return final_ans


if __name__ == "__main__":
    purchases = []
    with open("input.txt") as f:
        for line in f:
            purchases.append([purchase for purchase in line.strip().split(" ") if len(purchase) > 0])

    for _ in purchase_stats(purchases):
        print(_)
