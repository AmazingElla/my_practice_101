def fibonacci(n):
    a = 0
    b = 1
    even_sum = 0
    sequence = ""

    for i in range(n):
        sequence += str(a) + " "
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    reverse_sequence = ""
    a = 0
    b = 1
    for i in range(n):
        reverse_sequence = str(a) + ", " + reverse_sequence
        a, b = b, a + b

    print("Sequence: ", sequence)   
    print("Sum of even numbers: ", even_sum)
    print("Reverse Sequence: ", reverse_sequence[:-2])

fibonacci(8)
fibonacci(10)
    