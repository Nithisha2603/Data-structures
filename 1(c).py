from itertools import combinations

list = [-1, 2, -3, 4, -7]

print("Positive combinations")

for i in range(1, len(list) + 1):
    for combo in combinations(list, i):
        if all(num > 0 for num in combo):
            print(combo)
