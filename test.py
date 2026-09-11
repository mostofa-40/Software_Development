s = input().strip()
a = 0
b = 0
ss = ""
ans = []
for ch in s:
    ss += ch
    if ch == 'L':
        a += 1
    elif ch == 'R':
        b += 1
    if a == b:
        ans.append(ss)
        ss = ""
        a = 0
        b = 0
print(len(ans))
for x in ans:
    print(x)
