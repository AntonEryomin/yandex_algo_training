m, n, l, k = list(map(int, input().split()))


def get_min_square(m: int, n: int, l: int, k: int) -> int:
    return min([[max(m, l),(n+k)], [max(m, k), (n+l)], [max(n, l), (m+k)], [max(n, k), (m+l)]], key=lambda x: x[0]*x[1])


min_square = get_min_square(m,n,l,k)
print(f"{min_square[0]} {min_square[1]}")
