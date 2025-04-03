# Factorial Program using while loop
"""
num = int(input("Enter the number of your choice: "))
iterator = 0 # set to 0 for convience, to make iterations work properly and as expected
factorial = 1 
# We want to start multiplying from 1, because this is how mainly factorial works 
# and you don't want to multiply everything to 0

while iterator != num:
    iterator += 1
    factorial *= iterator
    print(f"{iterator}st iteration = {factorial}") # Just made this for your convenience to foster better understanding

print(f"The factorial of {num} is {factorial}")


# Factorial Program using for loop

n = int(input("Enter the number of your choice: "))
result = 1
# Why n+1? Because n is excluded and the range() behaves like this without n+1 (int i = 1; i < n; i++)
# That's why we wanna actually it to be like this: (int i = 1; i <= n; i++), to achieve this behavior, we just made n+1
for i in range(1, n+1): 
    result *= i
    print(f"The factorial of {i}! = {result}")

    
# The sum of factorials program

n = int(input("Enter the number of your choice: "))
result = 1
sum = 0
# Why n+1? Because n is excluded and the range() behaves like this without n+1 (int i = 1; i < n; i++)
# That's why we wanna actually it to be like this: (int i = 1; i <= n; i++), to achieve this behavior, we just made n+1
for i in range(1, n+1): 
    result *= i
    sum += result
    print(f"The factorial of {i}! = {result}")

print(f"The sum of factorials = {sum}")    


# Raise the user entered number to user entered exponent

x = int(input("Enter the base number: "))
y = int(input("Enter the exponent: "))
def raise_by_exponent(a, b):
    result = a**b
    return f"The {a} raised by {b} = {result}"

print(raise_by_exponent(x, y))"""

"""
# Converting decimal number to octal number 
# 1. Divide number by 8, until it doesn't become = 0: while num != 0: num = num // 8
# 2. sum remainders and also raise numbers msb or digit to create new_num
# 3. now we need to reverse the new_num

num = int(input("Enter the number: "))
decimal_num = num
remainder = 0
octal_num = 0
new_num = 0
while num != 0:
    remainder = num % 8
    new_num = (new_num * 10) + remainder
    num = num // 8
# now reversing the new number
# reverse_number = 0; reverse_number = reverse_number * 10 + last_digit
while new_num != 0:
        digits = new_num % 10
        octal_num = (octal_num * 10) + digits
        new_num = new_num // 10

print(f"The given decimal number {decimal_num} in octal form = {octal_num}")  


# Decimal to Binary Program
num = int(input("Enter the number: "))
decimal_num = num
remainder = 0
binary_num = 0
new_num = 0
while num != 0:
    remainder = num % 2
    if remainder <= 1:
        new_num = (new_num * 10) + remainder
    num = num // 2
    print(num) # To just see the quotients and division process
# now reversing the new number
# reverse_number = 0; reverse_number = reverse_number * 10 + last_digit
while new_num != 0:
        digits = new_num % 10
        binary_num = (binary_num * 10) + digits
        new_num = new_num // 10

print(f"The given decimal number {decimal_num} in binary form = {binary_num*10}") 
"""

# Sum of the first N Fibonnaci Numbers
# 1. Create the prev1, prev2 variables that starts with 0 and 1, because Fibonnaci Sequence starts with 0 and 1
# 2. New Fibonnaci number = prev1 + prev2
# 3. Assign the prev1 = prev2 and prev2 = fibonnaci_number 
# 4. sum += fibonnaci_number
"""
num = int(input("Enter the number: "))

def sum_of_n_fibonnaci_numbers(n: int):
    prev1 = 0
    prev2 = 1
    fibonnaci = 0
    sum = prev1 + prev2 # because it should firstly start with 0 + 1 and goes so on

    for i in range(1, n):
        fibonnaci = prev1 + prev2 
        print(f"The {i} new fibonnaci number = {fibonnaci}")
        prev1, prev2 = prev2, fibonnaci
        sum += fibonnaci
    return f"Sum of first {n} Fibonnaci numbers = {sum}"   

print(sum_of_n_fibonnaci_numbers(num))"""

# Check whether given number is armstrong number
# To find an Armstrong number, you need to calculate the sum of each digit raised to the power of the number of digits in the given number 
# and check if this sum equals the original number.
# For example, 153 is an Armstrong number because 1^3+5^3+3^3 = 153

"""num = int(input("Enter the number: ")) 
power = len(str(num))
def is_armstrong(n: int):
    sum_of_num_digits = 0
    given_num = n
    while n != 0:
        digit = n % 10
        sum_of_num_digits += digit**power
        n = n // 10
    print(sum_of_num_digits)    

    if sum_of_num_digits == given_num:
        return f"The given number {given_num} is armstrong number"
    else:
        return f"The given number {given_num} is not armstrong number"  

print(is_armstrong(num)) """

# Number Guessing Game Hard Mode
import random
random_num = random.randint(1, 100)
ATTEMPTS = 4
guess_num = int(input("Try to guess number between 1 and 100: "))

# The outer conditionals statements were made for validation check, sadly for now IDK how to Handle Exceptions, so I need to practice it
if guess_num >= 1 and guess_num <= 100:
    while ATTEMPTS != 0:
        if guess_num > random_num: print("Too High")
        else: print("Too low")
        print(f"You have {ATTEMPTS} attempts left.")
        ATTEMPTS -= 1
        guess_num = int(input("Try to guess number between 1 and 100 again: ")) 
    if guess_num == random_num:
        print(f"Horray, You Have guessed the number {random_num}")
    else:
        print(f"Game over! The correct number was {random_num}")           
else:
    print("Whoops, probaby entered invalid value!")
    guess_num = int(input("Please enter the number between 1 and 100 again: ")) 





