def count_even_in_range(numbers):
    count = 0

    for num in numbers:
        if num % 2 == 0 and num >= 10 and num <= 20:
            count += 1
    return count

print(count_even_in_range([8, 10, 12, 15, 18, 20, 22]))
print(count_even_in_range([4, 10, 12, 15, 18, 20, 22, 25]))