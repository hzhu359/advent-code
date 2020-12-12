
def main():
    fin = open('input.txt', 'r')
    # fin = open('new.txt', 'r')
    ret = 0
    idList = []
    for line in fin.readlines():
        line = line.strip()
        row = int(toBinaryString(line[0:7], ('F', 'B')), base=2)
        seat = int(toBinaryString(line[7:], ('L', 'R')), base=2)
        seatID = row * 8 + seat
        idList.append(seatID)
        ret = max(ret, seatID)
        # print("row: {}, seat: {}".format(rowBinary, seatBinary))
    idList = sorted(idList)
    missingId = -1
    for idx, idd in enumerate(idList):
        if not (idList[idx + 1] == idd + 1):
            missingId = idd + 1
            break
    print(missingId)
    # print(ret)

def toBinaryString(string, zeroOneTuple):
    zero = zeroOneTuple[0]
    one = zeroOneTuple[1]
    ret = ""
    for char in string:
        ret += "1" if (char == one) else "0"
    return ret

if __name__ == "__main__":
    main()