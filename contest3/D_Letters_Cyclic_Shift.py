s = input()
res = [0, 0]
weigh_of_change = 0

def swap(start, end, string):
    sascii = []
    for i in range(len(string)-1):
        sascii.append(ord(string[i]))
    for ind in range(start, end):
        if sascii[ind] == 97:
            sascii[ind] = 122
        else:
            sascii[ind] -= 1
    for ii in range(len(string) - 1):
        sascii[ii] = chr(sascii[ii])
    res = "".join(sascii)
    return res

for str_len in range(len(s)):
    for starting_str in range(len(s)-str_len):
        weigh = len(s[starting_str:(starting_str+str_len)])-s[starting_str:(starting_str+str_len)].count('a')
        if weigh > weigh_of_change:
            weigh_of_change = weigh
            res[0] = starting_str
            res[1] = starting_str+str_len

print(swap(res[0], res[1], s))


# print(ord('a'))
# print(ord('z'))