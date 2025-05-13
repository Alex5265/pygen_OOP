def is_correct_bracket_sequence(sequence):
    count = 0
    for char in sequence:
        count = count + 1 if char == '(' else count - 1
        if count < 0:
            return False
    return count == 0

print(is_correct_bracket_sequence(input()))