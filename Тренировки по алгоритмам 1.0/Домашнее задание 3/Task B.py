# Считываем ввод
nums_1 = set(input().split(" "))
nums_2 = set(input().split(" "))

print(" ".join(sorted(list(nums_1.intersection(nums_2)))))