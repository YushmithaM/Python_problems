def Measured_Array(arr, n):
    modi = sorted(arr)
    sanity = []
    i = 0
    while i < n:
        j = n-1
        while arr[i] != modi[j]:
            j = j-1
        sanity.append(i+j)
        i = i+1
    '''count_dict = { }
    for i in range(n):

        j = modi.index(arr[i], count_dict.get(arr[i], 0))
        sanity.append(i+j)


        count_dict[arr[i]] = j + 1'''


    measure = sum(sanity)
    return measure

arr = list(map(int,input("enter the list: ").split()))
n = len(arr)
res = Measured_Array(arr, n)
print(res)
