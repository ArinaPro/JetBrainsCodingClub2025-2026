n, m, cp = input().split()
# matrix = [[]*n]
n,m = int(n), int(m)

# for _ in range(n):
#     inprow = input()
#     for r in range(m):
#         matrix[r].append(inprow[r])
#
# res_colours = set()
#
# for row in range(n):
#     for column in range(m):
#         mrs = matrix[row][column]
#         mrs_row = matrix[row+1][column]
#         mrs_col = matrix[row][column+1]
#         if mrs_row != mrs_col and (cp in [mrs_row, mrs_col]):
#             if mrs_row == cp:
#                 res_colours.add(mrs_col)
#             else:
#                 res_colours.add(mrs_row)
#
#         # if mrs_row != cp:
#         #     if mrs == cp:
#         #         res_colours.add(mrs_row)
#         #     else:
#         #         res_colours.add(mrs)
#         # elif mrs == cp and mrs_col != cp:
#         #     res_colours.add(mrs_col)

table = [-1, -1]
matrix = []
res = set()

for ind in range(n):
    matrix.append(input())
    f = cp in matrix[ind]
    if f:
        if table[0] == -1:
            table[0] = [ind, matrix[ind].find(cp)]
        table[1] = [ind, m-(matrix[ind][::-1].find(cp))-1]
    else:
        if table[1] != -1:
            break

x1 = table[0][0]
y1 = table[0][1]
x2 = table[1][0]
y2 = table[1][1]

for y_col in range(y1, y2+1):
    if x1 != 0:
        res.add(matrix[x1-1][y_col])
    if x2 != n-1:
        res.add(matrix[x2+1][y_col])

for x_col in range(x1, x2+1):
    if y1 != 0:
        res.add(matrix[x_col][y1-1])
    if y2 != m-1:
        res.add(matrix[x_col][y2+1])

if "." in res:
    print(len(res)-1)
else:
    print(len(res))




