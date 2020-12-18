import re
from functools import reduce
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    ret = 0
    for idx, line in enumerate(finArray):
        line = line.strip()
        line = line.replace(' ', '')
        ret += int(evalWhole(line))
    varLog('poop', bummy='dum', ret=ret)

def evalWhole(inp: str):
    if not ('(' in inp):
        return str(evalInParen(inp))
    openStack = []
    resOpen = -1
    resClose = -1
    for idx, c in enumerate(inp):
        if c == '(':
            openStack.append(idx)
        elif c == ')':
            resOpen = openStack.pop()
            resClose = idx
            break
    # by this point we have the indices of the open/closed parens to evaluate
    inp = inp[:resOpen] + evalWhole(inp[resOpen + 1:resClose]) + inp[resClose + 1:]
    return evalWhole(inp)



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

'''
pass something in w/o parentheses around or in
'''
def evalInParen(inp: str):
    splitList = re.split('(\*)', inp)
    numList = []
    opList = []
    for c in splitList:
        if c == '+' or c == '*':
            opList.append(c)
        else:
            numList.append(int(evalAdd(c)))
    ret = numList[0]
    currNumDex = 1
    for op in opList:
        currOp = opMap[op]
        ret = currOp(ret, numList[currNumDex])
        currNumDex += 1
    return ret

def evalAdd(inp: str):
    splitList = re.split('\+', inp)
    splitList = map(lambda x: int(x), splitList)
    return reduce(addOp, splitList)


def multOp(a, b):
    return a * b

def addOp(a, b):
    return a + b

opMap = {'*': multOp, '+': addOp}

if __name__ == "__main__":
    main()