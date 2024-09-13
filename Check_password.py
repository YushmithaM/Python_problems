def valid_password(str, n):
    if str[0].isdigit() or n < 4 or not str.isupper():
        return False

    for i in range(n):

        if str[i].isnumeric() or str[i].isupper():
            continue
        if str[i] == "_":
            return False

    return True



