n, k = list(map(int, input().split()))
programmers = list(map(int, input().split()))
programmers.sort()
count = 0

if min(programmers) <= 5-k and n>2:
    for programmer in range(len(programmers)):
        if programmers[programmer] > 5-k:
            count = programmer
            break
        elif programmer == n-1:
            count = programmer+1
            break

print(count//3)