import re
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = [int(i) for i in fin.readlines()]

    # for idx, line in enumerate(finArray):
    #     print(line)

    # preLen = 25
    arrLen = len(finArray)
    # for i in range(preLen, arrLen):
    #     if not findSum(finArray[i - 25 : i], finArray[i]):
    #         print(finArray[i])
    #         break
    targetNum = 1038347917
    resulti = -1
    resultj = -1
    for idx, num in enumerate(finArray):
        res = 0
        j = idx
        found = False
        while res < targetNum and j < arrLen:
            res += finArray[j]
            if res == targetNum:
                print("{} {}".format(idx, j))
                resulti = idx
                resultj = j
                found = True
                break
            j += 1
        if found:
            break
    resultArr = finArray[resulti : resultj + 1]
    print(max(resultArr))
    print(min(resultArr))
    print(max(resultArr) + min(resultArr))



def findSum(arr, target):
    arrLen = len(arr)
    for i in range(arrLen - 1):
        for j in range(i, arrLen):
            if (arr[i] + arr[j]) == target:
                return True
    return False
if __name__ == "__main__":
    main()