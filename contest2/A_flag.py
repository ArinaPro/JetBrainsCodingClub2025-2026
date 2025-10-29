n, m = map(int, input().split())
flag = []
res = "YES"

for _ in range(n):
    flag.append(list(str(input())))


for row in range(n):
    for colour in range(m):
        if row != n-1:
            if flag[row][colour] == flag[row+1][colour]:
                res = "NO"
                break
        if colour != m-1:
            if flag[row][colour] != flag[row][colour + 1]:
                res = "NO"
                break

print(res)
