from math import lcm

n = int(input())
nums = list(map(int, input().split()))
num0 = -1
res = "Yes"

for num in nums:
    while num % 2 == 0:
        num = num // 2
    while num % 3 == 0:
        num = num // 3
    if num0 == -1:
        num0 = num
    else:
        if num != num0:
            res = "No"
            break

print(res)
