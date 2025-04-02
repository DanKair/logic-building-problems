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

