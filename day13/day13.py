import re
from functools import reduce
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    early = int(finArray[0])
    ids = finArray[1].strip().split(',')
    a = []
    n = []
    for idx, idNum in enumerate(ids):
        if idNum == 'x':
            continue
        a.append(int(-1 * idx))
        n.append(int(idNum))
    varLog(cr=chinese_remainder(n,a))
    # start = early
    # res = -1
    # minutes = 0
    # while True:
    #     mods = list(map(lambda x: start % x, ids))
    #     varLog(minutes=minutes,mods=mods)
    #     if 0 in mods:
    #         res = ids[mods.index(0)]
    #         break
    #     start += 1
    #     minutes += 1
    # varLog(result=(res * minutes))


# not my code lmaooooo
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def varLog(**kwargv):
    """
    prints out all variables in the format:
    varname: varvalue

    parameters:
        **kwargv: a keyword argument vector in the form of 'varname'=var
    """
    ret = ""
    for key, value in kwargv.items():
        ret += (' || ' + key + ': ' + str(value))
    print(ret)

if __name__ == "__main__":
    main()