def count_positive(numbers):
    count = 0

    for num in numbers:
        if num > 0:
            count += 1
    return count

print(count_positive([-3, 5, 0, 8, -1, 12]))