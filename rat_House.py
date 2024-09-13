def consume(r , unit , arr, n):
    cap = r*unit
    if cap == 0:
        return -1

    tot = sum(arr)
    if tot < cap:
        return 0
    s = 0
    for i in range(n):
        s += arr[i]
        if s>= cap:
            break
    return i+1





