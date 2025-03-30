# Sum of all 2D array (3x3 Matrix) elements
"""
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum = 0
for x in arr:
    print(x)
    for j in x:
        sum += j
        print(f"The sum of {j} elements = {sum}")  """

# Pattern building problem
n = int(input("Enter the number till which loop will execute: "))
for i in range(0, n):
    i += 1
    for j in range(i):
        print("*", end=' ')
    print()