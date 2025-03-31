# Factorial Program using while loop
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

"""x = int(input("Enter the base number: "))
y = int(input("Enter the exponent: "))
def raise_by_exponent(a, b):
    result = a**b
    return f"The {a} raised by {b} = {result}"

print(raise_by_exponent(x, y))"""


