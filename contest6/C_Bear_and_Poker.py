from math import lcm

n = int(input())
nums = list(map(int, input().split()))
lcm_nums = lcm(*nums)
res = "Yes"

for dnum in nums:
    num = lcm_nums // dnum
    while num % 2 == 0:
        num = num // 2
    while num % 3 == 0:
        num = num // 3
    if num != 1:
        res = "No"
        break

print(res)
