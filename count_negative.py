def count_negative(numbers):
    count = 0

    for num in numbers:
      if num < 0:
         count += 1

    return count

print(count_negative([4, -2, -7, 0, 9, -1, 6]))