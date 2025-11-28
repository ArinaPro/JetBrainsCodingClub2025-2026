a, b = list(map(int, input().split()))
res = a
#a, b = [max(a, b), min(a, b)]
if b<=a:
    while a >= b:
        c = a//b
        res += c
        a = c + (a - c*b)
print(res)