from __future__ import annotations
import re
from functools import reduce

class Node:
    next: Node
    val: int

    def __init__(self, v: int):
        """
        constructor for Node
        """
        self.val = v

def main():
    # llist = '389125467'
    llist = '739862541'
    # turns = 10
    turns = 10000000 
    maxVal = 1000000

    origOrdering = [int(i) for i in llist] + [x for x in range(10, maxVal + 1)]
    lookup = {i : Node(i) for i in origOrdering}
    for i in range(len(origOrdering)):
        lookup[origOrdering[i]].next = lookup[origOrdering[(i + 1) % len(origOrdering)]]

    curr = lookup[origOrdering[0]]

    for i in range(turns):
        removed = curr.next
        curr.next = curr.next.next.next.next

        dest = curr.val - 1 if curr.val > 1 else maxVal
        while dest in [removed.val, removed.next.val, removed.next.next.val]:
            dest -= 1
            if dest < 1:
                dest = maxVal 
        destNode = lookup[dest]
        removed.next.next.next = destNode.next
        destNode.next = removed
        curr = curr.next
    ret = 1 
    oneNode = lookup[1]
    ret *= oneNode.next.val * oneNode.next.next.val
    varLog(ret=ret)
        


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