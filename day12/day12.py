import re
def main():
    fin = open('input.txt','r')
    # fin = open('new.txt', 'r')
    finArray = fin.readlines()
    wayx, wayy = 10, 1
    x,y = 0,0
    llist = []
    # currDir = 90 # clockwise postiive
    for idx, line in enumerate(finArray):
        line = line.strip()
        direction = line[0]
        magnitude = int(line[1:])
        if direction == "N":
            wayy += magnitude
        elif direction == "S":
            wayy -= magnitude
        elif direction == "E":
            wayx += magnitude
        elif direction == "W":
            wayx -= magnitude
        elif direction == "L":
            turns = magnitude // 90 % 4
            for _ in range(turns):
                temp = wayx
                wayx = -wayy
                wayy = temp
        elif direction == "R":
            turns = magnitude // 90 % 4
            for _ in range(turns):
                temp = wayx
                wayx = wayy
                wayy = -temp
        elif direction == "F":
            x += wayx * magnitude
            y += wayy * magnitude
        # print("x: {}, y: {}".format(x, y))
    print("x: {}, y: {}".format(x, y))
    print(abs(x) + abs(y))

if __name__ == "__main__":
    main()