import sys
S = raw_input()
L = len(S)
T = L / 2

for i in range(0, T):
    if S[i] == S[L-1]:
        L -= 1
        continue
    else:
        print "NO"
        sys.exit()

print "YES"
