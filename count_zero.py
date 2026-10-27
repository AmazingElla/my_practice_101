def count_zero(lst):
    count = 0
    for num in lst:
        if num == 0:
            count += 1

    return count

print(count_zero([1, 0, 2, 0, 3, 0, 0, 0, 4, 5, 0]))