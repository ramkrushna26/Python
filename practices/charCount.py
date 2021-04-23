
string="Do you wanna know my secret identity? I am Batman!"
cnt={}

for char in string.lower():
    cnt.setdefault(char, 0)
    cnt[char] = cnt[char] + 1

print(cnt)
