n, k = map(int, input().split())
a = list(map(int, input().split()))

# d = {}
#
# for a in al:
#     d.update({a:False})
#
# alice =[]
# stop = 0
#
# for a in al:
#

# alice += list(d.values()).count("A")

# print(f"{alice} {n-alice}")


# res = []
# ind = [n]
# for i in range(n):
#     if i+1 in a:
#         if i != 0:
#             res.append(res[i-1])
#         else:
#             res.append("A")
#         if i+1 == a[k]:
#             ind = [i]
#             break
#     else:
#         if i == 0 or res[i-1] != "B":
#             res.append("B")
#         else:
#             res.append("A")
#
# a = res.count('A')
# print(f"{a} {n-a}")


pointer = 0
alice = 0
counter = 0
alice_index = 0

for aind in a:
    # num = aind-1-pointer
    # alice += (num)//2
    if aind-1 != pointer:
        if (aind-1-counter) % 2 != 0:
            alice += 1
            alice_index = aind
    else:
        if aind-1 == alice_index:
            alice += 1
            alice_index = aind
    pointer = aind
    counter += 1

num = n-1-k
if 1 not in a:
    alice += num//2 + 1
else:
    alice += num//2

# if num%2 == 0 and num != 0:
#     alice += (num)//2
# else:
#     alice += num//2 + 1
# if 2 in a:
#     alice += 1


print(f"{alice} {n-alice}")



