n, m = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
l = {}
for _ in range(m):
    fruit = input()
    if fruit in l.keys():
        l[fruit] += 1
    else:
        l[fruit] = 1

list_count = list(l.values())
list_count.sort(reverse=True)

s_min = 0
s_max = 0

for ind in range(len(list_count)):
    s_max += list_count[ind]*prices[::-1][ind]
    s_min += list_count[ind]*prices[ind]

print(f"{s_min} {s_max}")