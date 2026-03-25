rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if i == 5 and j == 3:
            continue
        if j > 5:
            break
        print(j, end=" ")
    print()