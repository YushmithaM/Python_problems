def transform(s1, s2):
    dict1 = {}

    for char in s2:
        if char in dict1:
            dict1[char] +=1
        else:
            dict1[char] = 1

    for val in s1:
        if val in dict1:
            dict1[val] -= 1

    res = sum(dict1.values())

    return res
# Time complexity = O(n)