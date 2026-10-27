def count_outside_range(numbers):
    count = 0

    for num in numbers:
        if num < 10 or num > 20:
            count += 1
    return count

print(count_outside_range([5, 10, 15, 20, 21, 12, 9]))