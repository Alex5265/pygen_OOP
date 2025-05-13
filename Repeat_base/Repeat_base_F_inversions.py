def inversions(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range( len(sequence)):
            if i < j and sequence[i] > sequence[j]:
                count += 1
    return count

def inversions(seq):
    res, n = 0, len(seq)
    for i in range(n):
        for j in range(i + 1, n):
            if seq[i] > seq[j]:
                res += 1
    return res

sequence = [3, 1, 4, 2]

print(inversions(sequence))