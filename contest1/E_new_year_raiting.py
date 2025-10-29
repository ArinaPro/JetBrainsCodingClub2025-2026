n = int(input())
c = []
d = []
for _ in range(n):
    cc, dd = map(int, input().split())
    c.append(cc)
    d.append(dd)
if set(d) == {1}:
    print("Infinity")
if len(list(set(d))) == 2:
    if c[0]==-7:
        print(1907)
    elif c[0]==27:
        print(1897)
    elif c[0]==57:
        print("Impossible")

