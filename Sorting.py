#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    swaps = 0
    for j in range(n-1):
        if a[j]>a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swaps += 1
    numSwaps += swaps
    if swaps == 0:
        break
firstElement = a[0]
lastElement = a[n-1]
print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element: {}".format(firstElement))
print("Last Element: {}".format(lastElement))

