n = int(input())
x = int(input())
regular = [0, 1, 2]

# if mod6 == 0:
#     print(x)
# else:
#     if x ==

for iteration in range(1, n%6+1):
    if iteration%2 != 0:
        regular[0], regular[1] = regular[1], regular[0]
    else:
        regular[2], regular[1] = regular[1], regular[2]
print(regular[x])