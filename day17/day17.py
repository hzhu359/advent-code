import re
import copy

def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    # 1 is active, 0 is inactive
    activeSet = set()
    arrLen = len(finArray)
    for idx, line in enumerate(finArray):
        line = line.strip()
        for jdx, char in enumerate(line):
            if char == '#':
                activeSet.add((idx, jdx, 0, 0))
    oldSet = set(activeSet)
    
    for it in range(6):
        for idx in range(0 - it - 1, arrLen + it + 1):
            for jdx in range(0 - it - 1, arrLen + it + 1):
                for zdx in range(0 - it - 1, 0 + it + 2):
                    for wdx in range(0 - it - 1, 0 + it + 2):
                        isActive = (idx, jdx, zdx, wdx) in oldSet
                        currCount = exploreAround((idx, jdx, zdx, wdx), oldSet)

                        if isActive:
                            if not (currCount == 2 or currCount == 3):
                                activeSet.remove((idx, jdx, zdx, wdx))
                        else:
                            if currCount == 3:
                                activeSet.add((idx, jdx, zdx, wdx))
        oldSet = set(activeSet)
    
    varLog(ret=len(activeSet))


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

def exploreAround(coord: tuple, activeSet: set):
    ci = coord[0]
    cj = coord[1]
    cz = coord[2]
    cw = coord[3]


    ret = 0
    for i in range(-1, 1 + 1):
        for j in range(-1, 1 + 1):
            for z in range(-1, 1 + 1):
                for w in range(-1, 1 + 1):
                    if i == j == z == w == 0:
                        continue
                    if not (ci + i, cj + j, cz + z, cw + w) in activeSet:
                        continue
                    else:
                        ret += 1
    return ret



if __name__ == "__main__":
    main()