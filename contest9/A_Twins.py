n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
s = sum(a)/2
cur = 0

for i in range(n):
    cur += a[i]
    if cur > s:
        print(i+1)
        break

