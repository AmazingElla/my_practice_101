def count_in_range(numbers):
    count = 0

    for num in numbers:
        if num >= 10 and num <= 20:   #if 10 <= num <= 20:  #if 20 >= num >= 10:
            count += 1
    return count

print(count_in_range([5, 10, 15, 20, 21, 12, 9]))