result = []
count = 0

for name in open(0):
    if name.strip() not in result:
        result.append(name.strip())
    else:
        count += 1

print(count)