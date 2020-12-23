import re
from functools import reduce
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.read()
    p1 = re.split('\n\n', finArray)[0]
    p1 = re.findall('(?:Player [0-9]:\n)?([0-9]+)', p1)
    p1 = list(map(lambda x: int(x), p1))
    p1 = list(reversed(p1))

    p2 = (re.split('\n\n', finArray)[1])
    p2 = re.findall('(?:Player [0-9]:\n)?([0-9]+)', p2)
    p2 = list(map(lambda x: int(x), p2))
    p2 = list(reversed(p2))
    # varLog(p1, p2)
    p1Won = play(p1, p2, 0)
    if p1Won:
        varLog(FINALRET=scoreFunc(p1))
    else:
        varLog(FINALRET=scoreFunc(p2))


def play(p1: list, p2: list, gameLevel: int):
    scoreSet = set()
    while p1 and p2:
        currScores = (tuple(p1), tuple(p2))
        # currScores = (scoreFunc(p1), scoreFunc(p2))
        if currScores in scoreSet:
            return True
        scoreSet.add(currScores)
        # varLog(p1=p1, p2=p2)
        curr1 = p1.pop()
        curr2 = p2.pop()

        p1Won = None
        win = None
        lose = None

        if len(p2) >= curr2 and len(p1) >= curr1:
            p1Won = play(p1[len(p1) - curr1:], p2[len(p2) - curr2:], gameLevel + 1)

        if not (p1Won is None):
            if p1Won:
                win = curr1
                lose = curr2
            else:
                win = curr2
                lose = curr1
        else: # if p1 is None
            win = max(curr1, curr2)
            lose = min(curr1, curr2)

        if win == curr1:
            p1.insert(0, win)
            p1.insert(0, lose)
        else:
            p2.insert(0, win)
            p2.insert(0, lose)

    # varLog(gameLevel=gameLevel,p1=p1, p2=p2)
    p1Won = True if p1 else False 
    # varLog(ret=scoreFunc(p1 if p1Won else p2))
    return p1Won

    # use a queue: enqueue at front, dequeue at back
    # for idx, line in enumerate(finArray):
    #     line = line.strip()
    #     print(line)

def scoreFunc(arr):
    ret = 0
    for idx, card in enumerate(arr):
        ret += (idx + 1) * card
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