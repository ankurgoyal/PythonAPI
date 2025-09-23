import math

def is_prime(n):
    if n <= 1:
      return False

    for i in range(2, int(math.sqrt(n)) + 1):
      if n % i == 0:
          return False
    return True

def print_prime_in_range(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for number in range(start, end + 1):
        if is_prime(number):
          print(number)      # Print the prime number  

print_prime_in_range(1, 100)