n = int(input())
a = input()
moon_sizes = "0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1"
# moon_sizes = moon_sizes.split(" ")

if n == 1:
    if a == '15':
        print("DOWN")
    elif a == '0':
        print("UP")
    else:
        print(-1)
else:
    l = a.split()
    if ( l[n-1] == '15' or int(l[n-1]) < int(l[n-2]) ) and l[n-1] != '0':
        print("DOWN")
    else:
        print("UP")