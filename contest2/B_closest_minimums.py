n = int(input())
a = list(map(int, input().split()))


m = min(a)
indm = a.index(m)
leng = float('inf')

for ind in range(indm+1, n):
    if a[ind] == m:
        if ind-indm < leng:
            leng = ind-indm
        indm = ind

print(leng)