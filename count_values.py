def count_passes(scores):
    count = 0

    for score in scores:
        if score >= 50:
            count += 1
    return count

print(count_passes([45, 72, 30, 85, 60, 38, 90]))
print(count_passes([65, 27, 20, 34, 80, 83, 100]))