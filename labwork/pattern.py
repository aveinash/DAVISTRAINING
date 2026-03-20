# Pattern printing with conditions


rows = 4

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if i % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()