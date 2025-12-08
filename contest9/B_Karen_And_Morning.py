time = input()
h = int(time[:2])
m = int(time[3:])

if 0 < h >= 10:
    h2 = int(str(h)[1] + str(h)[0])
else:
    h2 = int(str(h) + "0")

if 19>h>15 or (h==15 and h2-m < 0):
    print(60*(20-h) - m + 20)
elif 9>h>5 or (h==5 and h2-m < 0):
    print(60 * (10 - h) - m + 1)
else:
    if h2-m >= 0:
        print(h2-m)
    else:
        if h!=23 and h!=0:
            print(60-m+h2)
        elif h == 0:
            print(60+10-m)
        else:
            print(60-m)
