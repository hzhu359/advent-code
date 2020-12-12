import re
import queue
def main():
    fin = open('input.txt', 'r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    bagDict = {}
    for idx, line in enumerate(finArray):
        line = line.strip()
        line = line.split(' bags contain ')
        container = line[0]
        inside = line[1]
        bagDict[container] = inside
        inside = inside.replace('.', '')
        inside = inside.split(', ')
        for i, bag in enumerate(inside):
            if bag == 'no other bags':
                inside[i] = (0,0)
            else:
                bag = bag.replace('bags', '')
                bag = bag.replace('bag', '')
                regex = re.search('([0-9]) (.*)', bag)
                inside[i] = (regex[2].strip(), int(regex[1]))
        bagDict[container] = inside
    res = dfs(bagDict, 'shiny gold')
    print(res - 1)
    
def dfs(bagDict, curr):
    currEntry = bagDict[curr]
    print("curr: {}, currENtry: {}".format(curr, currEntry))
    if (0, 0) in currEntry:
        print("curr: {}, bazinga".format(curr))
        return 1
    ret = 0
    for x in currEntry:
        ret += x[1] * dfs(bagDict, x[0])
    print("curr: {} and: {}".format(curr, ret))
    return ret + 1

if __name__ == "__main__":
    main()

