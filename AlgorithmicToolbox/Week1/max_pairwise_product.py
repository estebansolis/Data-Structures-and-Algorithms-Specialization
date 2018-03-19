#python3
import sys

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

index = 0

for i in range(0,n):
    if a[i] > a[index]:
        index = i

value = 0

for j in range(0,n):
    if a[j] > value and j != index:
        value = a[j]

print(a[index] * value)