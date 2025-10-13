import math

n = int(input())
t = list(map(int, input().split()))

la = 0
sum_a = 0
# stop_a = False
# lb = 0
# sum_b = 0
# stop_b = False
s = sum(t)
midle_ch = 0
ch_ind = 0

while sum_a+t[ch_ind] <= (s/2):
    sum_a += t[ch_ind]
    la += 1
    ch_ind += 1
else:
    midle_ch = t[ch_ind]

sum_b = s-sum_a
lb = n-la

if sum_a == s/2:
    print(f"{la} {la}")
else:
    lb -= 1
    sum_b -= midle_ch
    if sum_a > sum_b:
        print(f"{la} {lb + 1}")
    elif sum_a <= sum_b:
        print(f"{la+1} {lb}")





# if sum_a > sum_b:
#     print(f"{n-lb-1} {lb+1}")
# elif sum_a < sum_b:
#     print(f"{la+1} {n-la-1}")
# else:
#     if sum_a == (s/2):
#         print(f"{la} {n-la}")
#     else:
#         print(f"{la+1} {n - la - 1}")