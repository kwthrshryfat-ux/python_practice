# Number Analyzer
# A simple Python program that analyzes numbers.


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

number = get_int("Enter your number: ")


# positive, negetive or Zero
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Even or Odd
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Digit Count
count = 0
n = abs(number)
count = 1 if n == 0 else 0
while n > 0:
    n //= 10
    count += 1

print("Digit count:", count)

# Digit sum
total = 0
n = abs(number)
while n > 0:
    total += n % 10
    n //= 10
print("Digit sum:", total)

# GCD
a = abs(number)
b = abs(get_int("Enter another number:"))
while b != 0:
    a, b = b, a % b

print("GCD:", a)


