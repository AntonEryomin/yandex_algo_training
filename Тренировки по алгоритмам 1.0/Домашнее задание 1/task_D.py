a = int(input())
b = int(input())
c = int(input())


def equation_solver(a: int, b: int, c: int) -> None:
    if c < 0:
        print("NO SOLUTION")
        return None
    if a == 0:
        if c ** 2 == b:
            print("MANY SOLUTIONS")
            return None
        else:
            print("NO SOLUTION")
            return None

    answer = (c**2 - b) / a

    if (c**2 - b) % a != 0:
        print("NO SOLUTION")
        return None
    else:
        print(int(answer))
        return None


equation_solver(a, b, c)
