import re
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.read().split(',')
    finArray = list(map(lambda x: int(x), finArray))
    # format: spoken: list of turns spoken (appended to end)
    bound = 30000000
    hMap = {}
    stack = []
    res = []
    arrLen = len(finArray)
    for idx, entry in enumerate(finArray):
        varLog(curr=entry)
        hMap[entry] = [idx + 1]
        stack.append(entry)
        res.append(entry)
    # varLog( hMap=hMap, stack=stack)
    for idx in range(arrLen + 1, bound + 1):
        curr = stack.pop()
        if len(hMap[curr]) > 1:
            # then we've seen it before
            mapArrLen = len(hMap[curr])
            diff = hMap[curr][mapArrLen - 1] - hMap[curr][mapArrLen - 2]
            if not diff in hMap:
                hMap[diff] = []
            hMap[diff].append(idx)
            stack.append(diff)
            res.append(diff)
        else:
            # we haven't seen it before
            hMap[0].append(idx)
            stack.append(0)
            res.append(0)
        # varLog(curr=curr, hMap=hMap, stack=stack)
    varLog(res=res[len(res) - 1])
    # for idx, line in enumerate(finArray):
    #     line = line.strip()
    #     print(line)

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