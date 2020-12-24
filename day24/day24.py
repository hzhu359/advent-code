import re
from functools import reduce
import copy
from numpy import linspace

directionDict = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (0.5, 1),
    'sw': (-0.5, -1),
    'nw': (-0.5, 1),
    'se': (0.5, -1)
}

def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()

    blackSet = set()
    for idx, line in enumerate(finArray):
        line = line.strip()
        line = re.split('(e|se|sw|w|nw|ne)', line)
        line = list(filter(lambda x: x, line))
        orig = (0, 0, 0)
        for direc in line:
            orig = elemAdd(directionDict[direc], orig)
        if orig in blackSet:
            blackSet.remove(orig)
        else:
            blackSet.add(orig)
    # steps = 10
    steps = 100

    for day in range(1, steps+1):
        newBlackSet = set() 
        whiteSet = set()
        # varLog(minx=minx, maxx=maxx, miny=miny, maxy=maxy)
        for x, y in blackSet:
            neighborList = set(retNeighbors(x, y))
            blackNeighbors = blackSet & neighborList
            whiteNeighbors = neighborList - blackSet
            whiteSet.update(whiteNeighbors)
            numBlack = len(blackNeighbors)
            if numBlack == 1 or numBlack == 2:
                newBlackSet.add((x,y))
        for x, y in whiteSet:
            neighborList = set(retNeighbors(x, y))
            blackNeighbors = blackSet & neighborList
            numBlack = len(blackNeighbors)
            if numBlack == 2:
                newBlackSet.add((x,y))
        blackSet = copy.deepcopy(newBlackSet)
    varLog(ret=len(blackSet))

def retNeighbors(x, y):
    orig = (x,y)
    ret = []
    for dd in directionDict.values():
        ret += [elemAdd(orig, dd)]
    return ret

def countAdjBlack(x, y, blackSet):
    orig = (x,y)
    ret = 0
    for dd in directionDict.values():
        result = elemAdd(orig, dd)
        ret += 1 if result in blackSet else 0
    return ret

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

def elemAdd(a, b):
    return tuple(map(lambda x: sum(x), zip(a, b)))

if __name__ == "__main__":
    main()