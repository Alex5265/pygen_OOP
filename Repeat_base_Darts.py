def drow_darts(pole):
    result = [[1] * pole for _ in range(pole)]
    for i in range(len(result)):
        for j in range(len(result[i])):
            result[i][j] = min( (i+1), (j+1), (len(result) - i), (len(result[i]) - j))
            print(result[i][j], end=' ')
        print()


num = int(input())
drow_darts(num)