def count_greater_than_five(numbers):
    count = 0

    for num in numbers:
        if num > 5:
            count += 1
    return count


print(count_greater_than_five([2, 5, 6, 8, 5, 10, 1]))