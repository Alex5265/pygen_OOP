import itertools

def intersperse(iterable, delimiter):

    for i, elem in enumerate(iterable):
        if i > 0:
            yield delimiter
        yield elem



print(*intersperse([1, 2, 3], 0))

inter = intersperse('beegeek', '!')
print(next(inter))
print(next(inter))
print(*inter)

print(*intersperse('A', '...'))