# Bubble sort (Needs optimization of shrinking window, however works as expected)
# 1. Traverse through the list
# 2. Do main outer loop while list is unsorted (the list[0] == min and list[last] == max)
# 3. if list[i] > list[i+1]: swap
# 4. Do it untill the largest element doesn't pop (reach the end)
# 5. Repeat the process for the next element

list = [12, 10, 9, 8, 7, 3, 1]
size = len(list)
while list != sorted(list):
    for i in range(size-1):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            print(list)

# Two Sum Problem
# 1. Find the target value
# 2. Traverse through the list
# 3. if sum == target: print(indeces)
# 4. sum should be addition of two elements together, but expect themself
# 5. each element should be checked with each other (like 0 index with 1-3 indexes, 1 index with 0, 2 and 3 indexes and etc)
nums = [2, 7, 11, 15]
target = 9
indexes = []

for i in range(len(nums)):
    sum = 0
    for j in range(i + 1, len(nums)): # i + 1 avoids comparing same pairs together (2,7 with 7,2 )
        sum = nums[i] + nums[j]
        print(f"Sum of {nums[i]} and {nums[j]} = {sum}")
        if sum == target:
            indexes.append(i)
            indexes.append(j)
print(f"The indexes are: {indexes}")


        