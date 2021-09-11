t_room, t_cond = list(map(int, input().split()))
mode = input()


def final_temperature(t_room: int, t_cond: int, mode: str) -> int:
    if mode == "fan":
        return t_room
    elif mode == "auto":
        return t_cond
    elif mode == "heat":
        if t_room >= t_cond:
            return t_room
        else:
            return t_cond
    elif mode == "freeze":
        if t_room > t_cond:
            return t_cond
        else:
            return t_room

print(final_temperature(t_room, t_cond, mode))
