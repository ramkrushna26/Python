
import sys
N = int(raw_input())

if 1< N <=1000:
    pass
else:
    sys.exit()

for num in range(2, N):
    np = True
    for i in range(2, num):
        if num % i == 0:
            np = False
            break
    
    if np == True:
        print num,
