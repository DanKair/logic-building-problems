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



        