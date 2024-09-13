def fequence_decrp(str,tar):
    res = " "
    n = len(str)
    for i in range(n-1):
        if str[0].isdigit():
            return "-1"

        if (not str[i].isdigit())  and  (str[i+1].isdigit()):
            res += (str[i]*int(str[i+1]))

    if tar >= len(res):
        return "-1"
    return res[tar]

s = input("enter string:")
tar = int(input("target number:"))
r = fequence_decrp(s,tar)
print(r)
# Time complexity : O(N)
# Space complexity: O(1)




