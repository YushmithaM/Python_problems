arr = list(map(int,input("Enter arr:").split(" ")))
n = len(arr)

def find_mini(arr, n):

    pos = []
    count = 0
    for i in range(n):
        if arr[i] > 0:
            pos.append(arr[i])
            count += 1

    mid = count//2
    if count%2 == 0:
        return min(pos[mid],pos[mid+1])
    return pos[mid]

result = find_mini(arr,n)
print(result)
