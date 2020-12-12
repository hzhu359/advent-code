import re
import copy
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    dupArray = []
    for idx, line in enumerate(finArray):
        toAdd = []
        line = line.strip()
        for char in line:
            toAdd.append(char)
        dupArray.append(toAdd[:])
    finArray = copy.deepcopy(dupArray)
    # print(finArray)
    # print(dupArray)
    n = len(dupArray)
    # print(n)
    m = len(dupArray[0])
    # print(m)
    occCount = 0
    change = True
    x = 0
    resStack = []
    # while x < 2:
    while change:
        x += 1
        occCount = 0
        change = False
        for i in range(n):
            for j in range(m):
                # print(i)
                # print(j)
                # if finArray[i][j] == '.':
                    # continue
                count = 0
                for k in range (i - 1, -1, -1):
                    if finArray[k][j] == 'L':
                        break
                    if finArray[k][j] == '#':
                        count += 1
                        break
                for k in range (i + 1, n, 1):
                    if finArray[k][j] == 'L':
                        break
                    if finArray[k][j] == '#':
                        count += 1
                        break
                for l in range (j - 1, -1, -1):
                    if finArray[i][l] == 'L':
                        break
                    if finArray[i][l] == '#':
                        count += 1
                        break
                for l in range (j + 1, m, 1):
                    if finArray[i][l] == 'L':
                        break
                    if finArray[i][l] == '#':
                        count += 1
                        break
                k,l = i - 1, j - 1
                while k >= 0 and k < n and l >= 0 and l < m:
                    if finArray[k][l] == 'L':
                        break
                    if finArray[k][l] == '#':
                        count += 1
                        break
                    k -= 1
                    l -= 1
                k,l = i - 1, j + 1
                while k >= 0 and k < n and l >= 0 and l < m:
                    if finArray[k][l] == 'L':
                        break
                    if finArray[k][l] == '#':
                        count += 1
                        break
                    k -= 1
                    l += 1
                k,l = i + 1, j - 1
                while k >= 0 and k < n and l >= 0 and l < m:
                    if finArray[k][l] == 'L':
                        break
                    if finArray[k][l] == '#':
                        count += 1
                        break
                    k += 1
                    l -= 1
                k,l = i + 1, j + 1
                while k >= 0 and k < n and l >= 0 and l < m:
                    if finArray[k][l] == 'L':
                        break
                    if finArray[k][l] == '#':
                        count += 1
                        break
                    k += 1
                    l += 1
                # print("i: {}, j:{}, count: {}".format(i, j, count))
                if finArray[i][j] == '#':
                    occCount += 1
                if finArray[i][j] == 'L' and count == 0:
                    # print("i: {}, j:{}, count: {}".format(i, j, count))
                    dupArray[i][j] = '#'
                    change = True
                elif finArray[i][j] == '#' and count >= 5:
                    dupArray[i][j] = 'L'
                    change = True
        # prettyPrint(dupArray)
        resStack.append(occCount)
        finArray = copy.deepcopy(dupArray)
    print(resStack)
                

def prettyPrint(arr):
    n = len(arr)
    m = len(arr[0])
    print()
    for i in range(n):
        for j in range(m):
            print(arr[i][j], end='')
        print()

if __name__ == "__main__":
    main()