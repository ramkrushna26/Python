#!/bin/python3

#
# Ramkrushna Bolewar
#
# This program calculate the product of numbers provided
# First it takes input N as number of numbers of which product you want
# Then takes T as input which are N numbers seperated by space
#

import sys

try:
    N = int(input("Enter the number: "))
except ValueError:
    print("Error: Provided incorrect input! ")
    sys.exit()

if 1 <= N <= 1000:
    pass
else:
    print("Error: Enter number between 1 and 1000!")
    sys.exit()
    
print("Enter " + str(N) + " numbers sepated by space: ", end="")
T = input().strip()
L = ''.join(T.split())
A = 1
for i in range(0, N):
    try:
        A = (A * int(L[i])) % (10**9 + 7)
    except IndexError:
        print("Error: You have entered less elements!")
        sys.exit()

print("Product of " + str(N) + " numbers: "  + str(A))
if N < len(L):
    print("Warning: You have entered more elements!")
