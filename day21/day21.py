import re
from functools import reduce
from collections import defaultdict
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    allergDict = {} 
    allIngr = set()
    counts = defaultdict(int)

    for idx, line in enumerate(finArray):
        line = line.strip()
        matches = re.split('\(contains (.+)\)', line)
        matches = list(filter(None, matches))
        # varLog(matches=matches)
        ingr = matches[0].strip().split(' ')
        allerg = matches[1].replace(' ','').strip().split(',')
        # varLog(ingr=ingr, allerg=allerg)

        # only keeps ingredients that show up each time an allergen is declared
        # filters using intersection (&)
        for i in ingr:
            counts[i] += 1
        allIngr.update(ingr)
        for a in allerg:
            if a in allergDict:
                allergDict[a] &= set(ingr)
            else:
                allergDict[a] = set(ingr)
    for _, v in allergDict.items():
        for ingr in v:
            counts[ingr] = 0
    ret = 0
    for _, v in counts.items():
        ret += v
    varLog(allergDict=allergDict)
    varLog(counts=counts)

    concrete = {}

    cont = True
    while cont:
        toRemove = None
        for allerg, ingrSet in allergDict.items():
            if len(ingrSet) == 1:
                toRemove = next(iter(ingrSet))
                concrete[allerg] = toRemove
                break
        if toRemove is None:
            break
        for allerg, ingrSet in allergDict.items():
            if toRemove in ingrSet:
                ingrSet.remove(toRemove)
    
    ret = ''
    sortedAllergs = sorted(concrete.keys())
    for allerg in sortedAllergs:
        ret += concrete[allerg] + ','
    varLog(ret=ret[:-1])

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