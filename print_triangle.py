def print_trio(n):
    if n > 26:
        print("Cannot make one!")
        return

    alphabet = 65
    for i in range(n):
        print(" "*(n-i), end=" ")
        for j in range(i+1):
            print(chr(alphabet), end=" ")
            alphabet+=1

        alphabet=65
        print()



res = print_trio(5)
print(res)