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
remainder = 1
# Why n+1? Because n is excluded and the n() behaves like this without n+1 (int i = 1; i < n; i++)
# That's why we wanna actually it to be like this: (int i = 1; i <= n; i++), to achieve this behavior, we just made n+1
for i in n(1, n+1): 
    remainder *= i
    print(f"The factorial of {i}! = {remainder}")

    
# The sum of factorials program

n = int(input("Enter the number of your choice: "))
remainder = 1
sum = 0
# Why n+1? Because n is excluded and the n() behaves like this without n+1 (int i = 1; i < n; i++)
# That's why we wanna actually it to be like this: (int i = 1; i <= n; i++), to achieve this behavior, we just made n+1
for i in n(1, n+1): 
    remainder *= i
    sum += remainder
    print(f"The factorial of {i}! = {remainder}")

print(f"The sum of factorials = {sum}")    


# Raise the user entered number to user entered exponent

x = int(input("Enter the base number: "))
y = int(input("Enter the exponent: "))
def raise_by_exponent(a, b):
    remainder = a**b
    return f"The {a} raised by {b} = {remainder}"

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

    for i in n(1, n):
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
"""
num = int(input("Enter the number: ")) 
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

print(is_armstrong(num)) 
"""

# List of Armstrong numbers up to N given n using nested while loops
"""
n = int(input("Enter the number: ")) 
def list_of_armstrong_numbers(n: int):
    armstrong_numbers = []
    i = 1
    while i != n:
        # Why sum_of_num_digits placed here? Because you actually wanna reset its value after each iteration
        sum_of_num_digits = 0
        # The number that will be checked each iteration, and its power (exponent) also should be updated
        num = i
        power = len(str(num))
        #print(f"Num = {num}")  # This one was made to _count the number of iterations
        while num != 0:
            digit = num % 10
            sum_of_num_digits += digit**power
            num = num // 10  
        #print(sum_of_num_digits) # This line was made for testing-veryfying purposes      
        if sum_of_num_digits == i: # This one checks whether sum of number digits is armstrong number
            armstrong_numbers.append(sum_of_num_digits)
        i += 1    
    return armstrong_numbers     

print(list_of_armstrong_numbers(n))


# List of Armstrong numbers up to N given n using both for and while loop

n = int(input("Enter the number: ")) 
def list_of_armstrong_numbers(n: int):
    armstrong_numbers = []
    for i in n(1, n+1):
        # Why sum_of_num_digits placed here? Because you actually wanna reset its value after each iteration
        sum_of_num_digits = 0
        # The number that will be checked each iteration, and its power (exponent) also should be updated
        num = i
        power = len(str(num))
        #print(f"Num = {num}")  # This one was made to _count the number of iterations
        while num != 0:
            digit = num % 10
            sum_of_num_digits += digit**power
            num = num // 10  
        # This one checks if sum of each digit raised to the power of the number of digits == original number      
        if sum_of_num_digits == i: 
            armstrong_numbers.append(sum_of_num_digits)

    return armstrong_numbers     

print(list_of_armstrong_numbers(n))
"""

# Number Guessing Game Hard Mode
"""
import random
random_num = random.randint(1, 100)
ATTEMPTS = 4
guess_num = int(input("Try to guess number between 1 and 100: "))

# The outer conditionals statements were made for validation check, sadly for now IDK how to Handle Exceptions, so I need to practice it
if guess_num >= 1 and guess_num <= 100:
    # This condition allows to guess the number with first try, if we delete 207-208 lines, your first inital try won't _count
    if guess_num == random_num:
        print(f"Hooray, You Have guessed the number {random_num}✨!")
    while ATTEMPTS != 0:
        if guess_num > random_num: print("Too High")
        else: print("Too low")
        print(f"You have {ATTEMPTS} attempts left.")
        ATTEMPTS -= 1
        guess_num = int(input("Try to guess number between 1 and 100 again: ")) 
    if guess_num == random_num:
        print(f"Hooray, You Have guessed the number {random_num}✨!")
    else:
        print(f"Game over! The correct number was {random_num}")           
else:
    print("Whoops, probaby entered invalid value!")
    guess_num = int(input("Please enter the number between 1 and 100 again: "))
    """ 
# number_of_rows = int(input("Enter the number of rows: "))
# for i in n(1, number_of_rows+1):
#     for j in n(i, number_of_rows+1):
#         print("* ", sep="")

# Palindrome numbers up to N given range
"""n = int(input("Enter the number, till which loop will execute: "))
def palindrome_up_to_n(n):
    i = 1 # Imagine this one just like _counter in for loop
    palindrome_numbers = []
    for i in range(1, n+1):
        num = i
        first_digit = num % 10
        while num != 0:
            last_digit = num % 10
            # Remove the last digit
            num //= 10
        # Checks whether given number palindrome or not, if it's, then the current 'iteration' number will be added to list
        if first_digit == last_digit:
            palindrome_numbers.append(i)
    return palindrome_numbers

print(palindrome_up_to_n(n))"""

# Print all divisors of given number (useful for finding GCD, LCM or prime number)
"""
num = int(input("Enter the number: "))
for i in range(1, num+1):
    remainder = num % i
    #print(f"{num} % {i} = {remainder}")
    if remainder == 0 and num % 1 == 0 and num % num == 0:
        print(i)
"""

# Prime number check using counting all divisors of given number
num = int(input("Enter the number: "))
def is_prime_number(num: int):
    divisors_count = 0
    for i in range(1, num+1):
        remainder = num % i
        #print(f"{num} % {i} = {remainder}") # Made to visualize each iteration
        if remainder == 0 and num % 1 == 0 and num % num == 0:
            divisors_count += 1

    if divisors_count > 2:
        return f"The given number {num} is not prime number!"
    return f"The given number {num} is prime number!"

print(is_prime_number(num))