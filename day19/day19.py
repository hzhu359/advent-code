import re
from functools import reduce
from itertools import product
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    rules = {} 
    inputs = []
    doRules = True
    for idx, line in enumerate(finArray):
        line = line.strip()
        if line == "":
            doRules = False
            continue
        if doRules:
            line = line.split(': ')
            ruleNum = int(line[0])

            ruleCont = line[1]
            ruleCont = ruleCont.split(' | ')
            if len(ruleCont) == 1:
                if 'a' in ruleCont[0]:
                    rules[ruleNum] = 'a'
                elif 'b' in ruleCont[0]:
                    rules[ruleNum] = 'b'
                else:
                    rules[ruleNum] = tuple([int(x) for x in ruleCont[0].split(' ')])
            else:
                ret = []
                for x in ruleCont:
                    ret.append(tuple([int(y) for y in x.split(' ')]))
                rules[ruleNum] = ret
        else:
            inputs.append(line)

    baseComps = []
    for idx, rule in enumerate(rules[0]):
        baseComps.append(dfs(rule, rules))
    baseComps = [x for x in product(*baseComps)]
    baseComps = set(map(combineIntoWord, baseComps))

    ret = 0
    for i in inputs:
        if i in baseComps:
            ret +=1
    varLog(ret=ret)

def dfs(curr: int, rules: dict):
    currRule = rules[curr]
    if 'a' in currRule:
        return ('a',)
    if 'b' in currRule:
        return ('b',) 
    if isinstance(currRule, tuple):
        ult = []
        for x in currRule:
            ult.append(dfs(x, rules))
        ult = [x for x in product(*ult)]
        return tuple(map(combineIntoWord, ult))
    if isinstance(currRule, list):
        ult = []
        for tup in currRule:
            subUlt = []
            for x in tup:
                subUlt.append(dfs(x, rules))
            # one = subUlt[0]
            # two = subUlt[1]
            subUlt = [x for x in product(*subUlt)]
            res = tuple(map(combineIntoWord, subUlt))
            ult.extend(res)
        return ult
        

def combineIntoWord(inp: tuple):
    ret = ''
    for i in inp:
        ret += i
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

if __name__ == "__main__":
    main()