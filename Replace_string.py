def trans(str1, n, ch1, ch2):
    res = ""
    for i in range(n):
        if str1[i] == ch1:
            res += ch2

        elif str1[i] == ch2:
            res += ch1
        else:
            res+= str1[i]

    return res
