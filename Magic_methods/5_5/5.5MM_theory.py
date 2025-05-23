m = [[1] * 5 for _ in range(4)]
m[0][1] = 2
m[1][2] = 2

for i in m:
    for j in i:
        print(j, end=' ')
    print()