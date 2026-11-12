def count_evens(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


print(count_evens([65, 27, 20, 34, 80, 83, 100]))
print(count_evens([3, 8, 11, 14, 20, 7, 6]))