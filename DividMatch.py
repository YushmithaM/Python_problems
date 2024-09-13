arr = list(map(int, input().split(" ")))
n = len(arr)
q = int(input("Qouient: "))
dis =  int(input("Divisor "))
r =  int(input("remainder: "))

def Match(arr,n,q,dis,r):
    div = (q * dis) + r
    for i in range(n):
        if arr[i] == div:
            return i
    return -1

result = Match(arr,n,q,dis,r)
print(result)



