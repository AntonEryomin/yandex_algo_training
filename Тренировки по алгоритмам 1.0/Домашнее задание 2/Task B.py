possible_sequence = ["CONSTANT", "ASCENDING", "WEAKLY ASCENDING", "DESCENDING", "WEAKLY DESCENDING", "RANDOM"]
deltas = set()

current = int(input())

while True:

    new_num = int(input())

    if new_num == -2*10**9:
        break
    elif new_num == current:
        deltas.add("constant")
    elif new_num > current:
        deltas.add("up")
    elif new_num < current:
        deltas.add("down")
    current = new_num

if len(deltas) == 3:
    print("RANDOM")
elif len(deltas) == 2:
    if deltas == set(['constant', 'up']):
        print("WEAKLY ASCENDING")
    elif deltas == set(['constant', 'down']):
        print("WEAKLY DESCENDING")
else:
    if set(["constant"]) == deltas:
        print("CONSTANT")
    elif set(["up"]) == deltas:
        print("ASCENDING")
    else:
        print("DESCENDING")
