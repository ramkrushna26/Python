import sys
N = int(input("Enter a number: "))

if 1 <= N <= 10000:
    pass
else:
    print("Error: Enter number between 1 and 10000!")
    sys.exit()
    
if N == 1:
    print("Patlu")
    sys.exit()

P = 1
while N > 0:
    M = P * 2
    if (N - P) <= M:
        print("Motu")
        break
    
    N = N - (P + M)
    P += 1
    if N <= P:
        print("Patlu")
        break
        
