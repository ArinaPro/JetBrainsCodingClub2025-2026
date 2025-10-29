n, m = map(int, input().split())
a = list(map(int, input().split()))
# max_days = 0


# def spase_food(food, mm):
#     #food - dict {TypeOfFood:HowManyThereAre}
#     #mm - current min
#     global n
#     global m
#     global max_days
#     if n > m:
#         return max_days
#     elif n == m:
#         max_days += 1
#         return max_days
#     else:
#         mm = min(food.values())
#         food22 = food
#         while len(food22) < n:
#             food22 = dict
#             for fk, fv in food.items():
#                 if fv == 0:
#                     continue
#                 elif fv == mm:
#                     food22.update({fk: fv})
#                 else:
#                     for i in range(1, mm//fv):
#                         food22.update({f"{fk}_{i}": n})
#                     food22.update({f"{fk}_{n//fv}": mm+(n%fv)})
#             mm -= 1
#         print(mm)
#         # if len(food22) > n:
#         # if len(food22) >= n:
#         #     max_days += mm
#         #     if len(food22) != 0:
#         #         max_days += spase_food(food22, mm)
#         # else:
#         #     max_days += 1
#         #     if len(food22) != 0:
#         #         max_days += spase_food(food22, 1)
#     return max_days
#
# # if n > m:
# #     pass
# # elif n == m:
# #     max_days = 1
# # else:
# #     s = set(a)
# #     d = dict()
# #     d2 = dict()
# #     for i in s:
# #         d.update({i:a.count(i)})
# #     max_days = min(d.values())
# #     for maxd in range(n, max_days, -1):
# #         for k, v in d.items():
# #             d2.update({k:(v-maxd)})
# #         if n < maxd:
# #             break
# #         elif n == m:
# #             max_days += 1
#
#
s = set(a)
food = dict()
for i in s:
    food.update({i:a.count(i)})


# print(spase_food(d, m))

if n > m:
    print(0)
elif n == m:
    print(1)
else:
    mm = min(food.values())
    food22 = food
    while len(food22) < n:
        food22 = dict
        for fk, fv in food.items():
            if fv == 0:
                continue
            elif fv == mm:
                food22.update({fk: fv})
            else:
                for i in range(1, mm // fv):
                    food22.update({f"{fk}_{i}": n})
                food22.update({f"{fk}_{n // fv}": mm + (n % fv)})
        mm -= 1
    print(mm)