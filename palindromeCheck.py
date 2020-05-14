
#
# Ramkrushna Bolewar
#
# This script check whether number is palindrome or not
#

import sys

S = input("Enter a number: ")
L = len(S)
T = L // 2

for i in range(0, T):
    if S[i] == S[L-1]:
        L -= 1
        continue
    else:
        print("Not a palindrome!")
        sys.exit()

print("Palindrome!")
