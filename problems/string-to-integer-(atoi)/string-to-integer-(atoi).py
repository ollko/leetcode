
def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    if not str:
        return 0
    elif not (str[0].isdigit() or str[0] in '+-'):
        return 0
    else:
        sign = 1
        start = 0
        if str[0] in '+-':
            start = 1
        if str[0] == '-':
            sign = -1        
        num = 0
        for i in range(start, len(str)):
            if str[i].isdigit():
                num = num*10 + int(str[i])
            else:
                break
        if sign < 0 and -num < -2**31:
            return -2**31
        elif sign > 0 and num > 2**31 - 1:
            return 2**31 - 1
        else:
            return num*sign