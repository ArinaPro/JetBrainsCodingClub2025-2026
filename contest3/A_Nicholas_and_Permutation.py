n = int(input())
a = list(map(int, input().split()))

ind_max = a.index(max(a))
ind_min = a.index(min(a))
print(max(ind_max, ind_min)-min(ind_min, ind_max)+max(min(ind_max, ind_min), n-1-max(ind_max, ind_min)))