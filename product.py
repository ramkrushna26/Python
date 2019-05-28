import sys

N = int(raw_input())
if 1 <= N <= 1000:
    pass
else:
    sys.exit()
    
T = raw_input()
A = 1
for i in range(0, N):
    A = (A * int(T.split(" ")[i])) % (10**9 + 7)
    
print A
