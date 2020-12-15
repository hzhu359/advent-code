import re
import copy
retMap = {}
poopCount = 0
def main():
    global retMap
    global poopCount
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.read().split('mask')
    finArray.remove('')
    finArrayLen = len(finArray)
    for idx in range(len(finArray)):
        curr = (finArray[idx]).split('\n')
        if not idx == finArrayLen - 1:
            curr.pop()
        currLen = len(curr)
        mask = re.search('[10X]+', curr[0])[0]
        curr[0] = mask
        for jdx in range(1, currLen):
            jcurr = curr[jdx]
            match = re.findall('([0-9]+)', curr[jdx])
            curr[jdx] = (int(match[0]), int(match[1]))
        finArray[idx] = curr
    # format is : [[strMask, (addr, val), (addr, val), ...], ...]
    for idx, entry in enumerate(finArray):
        # if idx == 1:
            # break
        mask = entry[0]
        setMask = int(mask.replace('X', '0'), 2) # OR
        xLocs = [m.span()[0] for m in re.finditer('X', mask)]
        varLog(entry=entry, setMask=setMask, xLocs = xLocs)
        # clearMask = int(mask.replace('X', '1'), 2)  # AND
        for jdx, jentry in enumerate(entry):
            if jdx == 0:
                continue
            addr = jentry[0]
            val = jentry[1]
            # curr &= clearMask
            addr |= setMask
            addr = '{:036b}'.format(addr)
            dfs(addr, val, xLocs, 0)
    
    ret = 0
    for key, value in retMap.items():
        ret += value
    varLog(ret=ret)
    varLog(poopCount=poopCount)




    # for idx, line in enumerate(finArray):
    #     line = line.strip()
    #     print(line)

def dfs(addr: str, val: int, xLocs: list, idx: int):
    global retMap
    global poopCount
    if idx == len(xLocs):
        retMap[int(addr, 2)] = val
        poopCount += 1
        return
    currDex = xLocs[idx]

    newAddr = addr[:currDex] + '0' + addr[currDex + 1:]
    # varLog(newAddr=newAddr, currDex=currDex, xLocs=xLocs)
    dfs(newAddr, val, xLocs, idx + 1)

    newAddr = addr[:currDex] + '1' + addr[currDex + 1:]
    # varLog(newAddr=newAddr, currDex=currDex, xLocs=xLocs)
    dfs(newAddr, val, xLocs, idx + 1)


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