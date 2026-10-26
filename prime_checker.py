def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True

is_prime_input = int(input("Enter a number to check if it is prime: "))
if is_prime(is_prime_input):
    print(f"{is_prime_input} is a prime.")
else:
    print(f"{is_prime_input} is not a prime.")

prime_list = [n for n in range(2, is_prime_input + 1) if is_prime(n)]
print(f"Primes up to {is_prime_input}: {prime_list}")

prime_sum = 0

for prime in prime_list:
    prime_sum += prime  
4
print(f"The sum of primes: {prime_sum}")
