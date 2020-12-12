def main():
    fin = open('input.txt', 'r')
    finString = fin.read()
    finArray = finString.split('\n\n')
    ret = 0
    for i, line in enumerate(finArray):
        curr = line.split('\n')
        print(curr)
        lineSet = set()
        for j in curr[0]:
            lineSet.add(j)
        for answer in curr:
            currSet = set()
            for j in answer:
                currSet.add(j)
            lineSet = lineSet.intersection(currSet)
        print("lineSet: {}, incr: {}".format(lineSet, len(lineSet)))
        ret += len(lineSet)

        # if (i == 10):
            # break
        # currSet = set()
        # for j in curr:
        #     currSet.add(j)
        # print(currSet)
        # ret += len(currSet)
    # print(finArray)
    print(ret)



if __name__ == "__main__":
    main()