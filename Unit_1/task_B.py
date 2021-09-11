a = int(input())
b = int(input())
c = int(input())


def is_triangle(a: int, b: int, c: int) -> str:
    if a > 0 and b > 0 and c > 0:
        if a + b > c and a + c > b and b + c > a:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

print(is_triangle(a, b, c))