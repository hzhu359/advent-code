import re
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    finLen = len(finArray)
    i = 0
    accumulator = 0
    iset = set()
    # terminate = False

    for idx in range(finLen):
        arrCopy = finArray[:]
        line = arrCopy[idx].strip()
        if ('jmp' in line) or ('nop' in line):
            if 'jmp' in line:
                line = line.replace('jmp', 'nop')
            elif 'nop' in line:
                line = line.replace('nop', 'jmp')
        else:
            continue
        print(finArray)
        arrCopy[idx] = line
        iset = set()
        i = 0
        accumulator = 0
        terminate = False
        while i < finLen:
            if i in iset:
                terminate = True
                break
            iset.add(i)
            curr = arrCopy[i].strip().split(' ')
            instr = curr[0]
            val = int(curr[1])
            # print("{} {}".format(instr, val))
            if instr == 'acc':
                accumulator += val
                i += 1
            elif instr == 'jmp':
                i += val
            else:
                i += 1
        if not terminate:
            break


    # while i not in iset:
    #     iset.add(i)
    #     curr = finArray[i].strip().split(' ')
    #     instr = curr[0]
    #     val = int(curr[1])
    #     # print("{} {}".format(instr, val))
    #     if instr == 'acc':
    #         accumulator += val
    #         i += 1
    #     elif instr == 'jmp':
    #         i += val
    #     else:
    #         i += 1

    print(accumulator)

if __name__ == "__main__":
    main()