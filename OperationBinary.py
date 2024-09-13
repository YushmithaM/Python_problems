def OperationBinString(string):
    if string is None:
        return -1
    if string[0] == '0' or string[0] == '1':
        num = int(string[0])
    if '0' not in string and '1' not in string:
        return -1

    for i in range(1,len(string)-1):
        if string[i] == 'A' and (string[i+1] == '0' or string[i+1] == '1'):
            num = (num& int(string[i+1]))
        elif string[i] == 'B' and (string[i+1] == '0' or string[i+1] == '1'):
            num = (num| int(string[i+1]))
        elif string[i] == 'C' and (string[i+1] == '0' or string[i+1] == '1'):
            num = (num^int(string[i+1]))
        else:
            return -1

    return num


