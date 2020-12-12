import re
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    finArray = [int(i) for i in finArray]
    finArray = sorted(finArray)
    arrLen = len(finArray)
    maxVal = finArray[arrLen - 1]
    # oneGap = 0
    # threeGap = 0
    # for i in range(0, arrLen - 1):
    #     diff = finArray[i + 1] - finArray[i]
    #     if diff == 1:
    #         oneGap += 1
    #     if diff == 3:
    #         threeGap += 1
    # print((oneGap + 1) * (threeGap + 1))
    dpArray = [1] + [0] * maxVal
    for i in finArray:
        if i == 1:
            dpArray[i] = dpArray[i - 1]
        if i == 2:
            dpArray[i] = dpArray[i - 1] + dpArray[i - 2]
        else:
            dpArray[i] = dpArray[i - 1] + dpArray[i - 2] + dpArray[i - 3]
        
    print(dpArray)


# def dfs(curr, target, numSet):
#     if not curr == 0 and not (curr in numSet):
#         return 0
#     if curr == target:
#         # print()
#         return 1
#     if curr > target:
#         return 0
#     # print(curr)
#     return dfs(curr + 1, target, numSet) + dfs(curr + 2, target, numSet) + dfs(curr + 3, target, numSet)

if __name__ == "__main__":
    main()