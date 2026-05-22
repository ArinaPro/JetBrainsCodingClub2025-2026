n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dif = set(a)&(set(b))

if dif:
    print(min(list(dif)))
else:
    print(f"{min(min(a), min(b))}{max(min(a), min(b))}")