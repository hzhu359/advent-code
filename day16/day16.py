import re
from functools import reduce
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    rules = finArray[0:finArray.index('your ticket:\n') - 1]
    your = finArray[finArray.index('your ticket:\n') + 1]
    nearby = finArray[finArray.index('nearby tickets:\n') + 1:]

    ruleMap = {}
    intervalSet = set()
    for idx in range(len(rules)):
        curr = rules[idx]
        curr = curr.strip()
        splitList = re.split(': | or ', curr)
        for jdx in range(1, len(splitList)):
            jcurr = re.split('-', splitList[jdx])
            splitList[jdx] = (int(jcurr[0]), int(jcurr[1]))
        ruleMap[splitList[0]] = splitList[1:]

    yourArr = re.split(',', your)
    yourArr = toIntMap(yourArr)

    for idx in range(len(nearby)):
        curr = nearby[idx].strip()
        curr = re.split(',', curr)
        curr = toIntMap(curr)
        nearby[idx] = curr
    # varLog(nearby=nearby)
    
    for key, value in ruleMap.items():
        for tup in value:
            intervalSet.update(list(range(tup[0], tup[1] + 1)))
    # varLog(intervalSet=intervalSet)

    keyCount = {}
    for key, value in ruleMap.items():
        keyCount[key] = {}
        for i in range(len(ruleMap.items())):
            keyCount[key][i] = 0
        currSet = set()
        for tup in value:
            currSet.update(list(range(tup[0], tup[1] + 1)))
        ruleMap[key] = currSet
    # varLog(ruleMap=ruleMap)

    # ret = 0
    removeIndices = []
    for idx, ientry in enumerate(nearby):
        for jdx, jentry in enumerate(ientry):
            if not (jentry in intervalSet):
                # ret += jentry
                removeIndices.append(idx)
                break
    removeIndices = removeIndices[::-1]

    for i in removeIndices:
        nearby.pop(i)

    for idx, ientry in enumerate(nearby):
        for jdx, jentry in enumerate(ientry):
            for key, value in ruleMap.items():
                if jentry in value:
                    keyCount[key][jdx] += 1

    for key, value in keyCount.items():
        compSet = set()
        for jkey, jvalue in value.items():
            if jvalue == len(nearby):
                compSet.add(jkey)
        keyCount[key] = compSet
    # varLog(keyCount=keyCount)

    resMap = {}
    while len(keyCount.items()) > 0:
        toRemove = -1
        for key, value in keyCount.items():
            if len(value) == 1:
                corrVal = next(iter(value))
                resMap[key] = corrVal
                toRemove = corrVal
                keyCount.pop(key)
                break
        for key, value in keyCount.items():
            # varLog(value=value)
            value.remove(toRemove)
    
    varLog(resMap=resMap)
    deptDexList = [val for key, val in resMap.items() if re.search('departure', key)]
    varLog(deptDexList=deptDexList)
    ret = reduce(lambda x, y: x * y, [yourArr[i] for i in deptDexList], 1)
    varLog(ret=ret)

    # for idx, line in enumerate(finArray):
    #     line = line.strip()
    #     varLog(idx=idx, line=line)
    # varLog(nearby=nearby)

def toIntMap(arr):
    return list(map(lambda x: int(x), arr))

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