
"""
At the beginning of the school year Berland State University starts two city school programming groups,
for beginners and for intermediate coders. The children were tested in order to sort them into groups.
According to the results, each student got some score from 1 to m points.
We know that c1 schoolchildren got 1 point, c2 children got 2 points, ..., cm children got m points.
Now you need to set the passing rate k (integer from 1 to m):
all schoolchildren who got less than k points go to the beginner group
and those who get at strictly least k points go to the intermediate group.

We know that if the size of a group is more than y, then the university won't find a room for them.
We also know that if a group has less than x schoolchildren,
then it is too small and there's no point in having classes with it.
So, you need to split all schoolchildren into two groups so that the size of each group was from x to y, inclusive.

Help the university pick the passing rate in a way that meets these requirements.
"""



m = int(input())
c = list(map(int, input().split()))
x, y = map(int, input().split())

k=0
sum_c = 0
sum_all = 0
for c_el in c:
    sum_all += c_el

for i in range(2, len(c)):
    sum_c += c[i-2]
    if x<=sum_c<=y and x<=sum_all-sum_c<=y:
        k = i
        break
print(k)