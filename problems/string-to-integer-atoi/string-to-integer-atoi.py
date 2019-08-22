
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


import re
def myAtoi1(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()
    if not str:
        return 0
    else:
        d = re.match(r'[+-]{0,1}\d+', str)
        if not d:
            return 0
        else:
            sign = 1
            if str[0] in '+-':
                if str[0] == '-':
                    sign = -1
                dstr = str[1:d.end()]
            else:
                dstr = str[:d.end()]

            res = 0
            for i in range(len(dstr)):
                res += int(dstr[i]) * 10**((len(dstr)-1)-i)
            if res*sign > 2**31 - 1:
                return 2**31 - 1
            elif res*sign < -2**31:
                return -2**31
            else:
                return res*sign

