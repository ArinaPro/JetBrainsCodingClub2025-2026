a, b = list(map(int, input().split()))
res = a
a, b = [max(a, b), min(a, b)]

while a > b:
    a = a//b
    res += a
    if a> b:
        a += a%b
if a == b:
    res += 1

print(res)