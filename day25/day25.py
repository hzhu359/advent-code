import re
from functools import reduce
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    cardPub = int(finArray[0])  
    doorPub = int(finArray[1])  
    varLog(c=cardPub, d=doorPub)
    cardLoop = transformFind(7, cardPub)
    doorLoop = transformFind(7, doorPub)
    varLog(cL = cardLoop, dL = doorLoop)
    cardEncryption = transform(doorPub, cardLoop)
    doorEncryption = transform(cardPub, doorLoop)
    varLog(cE=cardEncryption, dE=doorEncryption)

def varLog(*argv, **kwargv):
    """
    prints out all variables in the format:
    varvalue
    OR
    varname: varvalue
    parameters:
        *argv: a argument vector that prints out anything you want
        **kwargv: a keyword argument vector in the form of 'varname'=var
    """
    ret = ""
    for value in argv:
        ret += (' || ' + str(value))
    for key, value in kwargv.items():
        ret += (' || ' + key + ': ' + str(value))
    print(ret)

def transform(subNum, loopSize, div=20201227):
    ret = 1
    for _ in range(loopSize):
        ret *= subNum
        ret %= div
    return ret

def transformFind(subNum, target, div=20201227):
    ret = 1
    counter = 0
    while True:
        if ret == target:
            return counter
        counter += 1
        ret *= subNum
        ret %= div
    return -1

if __name__ == "__main__":
    main()
