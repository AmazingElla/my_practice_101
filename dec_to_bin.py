num = int(input("Enter a positive number here: "))


if num == 0:
    binary_str = "0"
else:
    binary_str = ""
    temp = num  

    while temp > 0:
        binary_str = str(temp % 2) + binary_str
        temp //= 2

print("Output: ", binary_str)
