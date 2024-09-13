def Next_gen(arr):

    n = len(arr)
    res = []
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] <= arr[j]:
                gen = arr[j]
                break
            else:
                gen = -1
        if i == n-1:
            gen = -1
        res.append(gen)

    return res