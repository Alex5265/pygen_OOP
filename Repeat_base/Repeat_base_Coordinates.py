for row in open(0):
    x,y = map(float, row.strip('\n()').split(', '))
    print(-90<=float(x)<=90 and -180<=float(y)<=180)