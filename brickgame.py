import sys
N = int(raw_input())

if 1 <= N <= 10000:
    pass
else:
    sys.exit()
    
if N == 1:
    print "Patlu"
    sys.exit()

P = 1
while N > 0:
    M = P * 2
    if (N - P) <= M:
        print "Motu"
        break
    
    N = N - (P + M)
    P += 1
    if N <= P:
        print "Patlu"
        break
        
