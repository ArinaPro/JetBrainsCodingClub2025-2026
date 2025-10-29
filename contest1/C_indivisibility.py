n = int(input())
l = list(range(1, n+1))
res = list(filter(lambda x: x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0, l))
print(len(res))