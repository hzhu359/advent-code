import re
from functools import reduce
import numpy as np
from collections import defaultdict
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    tiles = {}
    finArray = fin.read().split('\n\n')
    finArray = list(map(lambda x: x.split('\n'), finArray))
    for idx, i in enumerate(finArray):
        tileId = int((re.search('([0-9]+)', i[0])).group(0))
        listList = np.array(list(map(lambda x: list(x), i[1:]))) 
        tiles[tileId] = listList
    # varLog(tiles)
    # maps unique edges (i.e. min(edge, reverse(edge))) to occurrences
    edgeDict = defaultdict(int)
    for _, value in tiles.items():
        nsew = getEdges(value, None)
        for _, jvalue in nsew.items():
            edge = ''.join(jvalue)
            edgeDict[min(edge, edge[::-1])] += 1
    outers = set([k for k, v in edgeDict.items() if v == 1])
    inners = set([k for k, v in edgeDict.items() if v == 2])

    for key, value in edgeDict.items():
        varLog(edge=key, count=value)


    ret = 1
    for key, value in tiles.items():
        nsew = getEdges(value, None).values()
        outerCount = 0
        for k in nsew:
            kWord = ''.join(k)
            outerCount += 1 if kWord in outers or kWord[::-1] in outers else 0
        if outerCount == 2:
            ret *= key
        # varLog(outerCount)
    varLog(ret)


'''
returns an edge of the array
'''
def getEdges(arr: np.ndarray, direc: str = None):
    length = len(arr)
    switch = {
        'N': arr[0, :],
        'S': arr[length - 1, :],
        'E': arr[:, length - 1],
        'W': arr[:, 0]
    }
    if not direc:
        return switch
    else:
        return switch[direc]

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

if __name__ == "__main__":
    main()